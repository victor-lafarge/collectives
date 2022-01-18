""" Module for reservation related route

This modules contains the /reservation Blueprint
"""
from datetime import datetime
from flask_login import current_user
from flask import render_template, redirect, url_for
from flask import Blueprint, flash

from collectives.utils.access import user_is
from ..models import db
from ..models import Equipment, Event, RoleIds
from ..models.reservation import ReservationStatus, Reservation, ReservationLine
from ..forms.reservation import LeaderReservationForm

blueprint = Blueprint("reservation", __name__, url_prefix="/reservation")
""" Reservation blueprint

This blueprint contains all routes for reservations
"""


@blueprint.route("/", methods=["GET"])
def reservations():
    """
    Show all the reservations
    """
    reservation = Reservation()

    reservation.collect_date = datetime.now()
    reservation.return_date = datetime.now()
    reservation.user = current_user
    for y in range(1, 5):
        reservationLine = ReservationLine()
        reservationLine.quantity = y
        reservationLine.equipment = Equipment.query.get(y)
        reservation.lines.append(reservationLine)
    db.session.add(reservation)

    return render_template(
        "reservation/reservations.html",
        reservations=Reservation.query.all(),
    )


@blueprint.route("/<int:reservation_id>", methods=["GET"])
def reservation(reservation_id):
    """
    Shows a reservation
    """

    return render_template(
        "reservation/reservation.html",
    )


@blueprint.route("/add", methods=["GET"])
@blueprint.route("/<int:reservation_id>", methods=["GET"])
def manage_reservation(reservation_id=None):
    """Reservation creation and modification page.

    If an ``reservation_id`` is given, it is a modification of an existing reservation.

    :param int reservation_id: Primary key of the reservation to manage.
    """
    reservation = (
        Reservation()
        if reservation_id is None
        else Reservation.query.get(reservation_id)
    )

    form = (
        LeaderReservationForm()
        if reservation_id is None
        else LeaderReservationForm(obj=reservation)
    )
    action = "Ajout" if reservation_id is None else "Édition"

    if not form.validate_on_submit():
        return render_template(
            "basicform.html",
            form=form,
            title=f"{action} de réservation",
        )

    form.populate_obj(reservation)

    db.session.add(reservation)
    db.session.commit()

    return redirect(url_for("reservation.reservation", reservation_id=reservation_id))

@blueprint.route("/<int:event_id>/<int:role_id>/register", methods=["GET"])
def register(event_id=None, role_id=None):
    """Page for user to create a new reservation.

    The displayed form depends on the role_id, a leader can create an reservation without paying
    and without a max number of equipment.
    The reservation will relate to the event of event_id.

    :param int role_id: Role that the user wishes to register has.
    :param int event_id: Primary key of the related event.
    """
    role = RoleIds.get(role_id)
    if role is None:
        flash("Role inexistant", "error")
        return redirect(url_for("event.view_event", event_id=event_id))

    if not current_user.has_role([role_id]) and not current_user.is_moderator():
        flash("Role insuffisant", "error")
        return redirect(url_for("event.view_event", event_id=event_id))

    if not role.relates_to_activity():
        flash("Role not implemented yet")
        return redirect(url_for("event.view_event", event_id=event_id))

    event = Reservation() if event_id is None else Event.query.get(event_id)
    form = LeaderReservationForm()

    if not form.validate_on_submit():
        return render_template(
            "reservation/editreservation.html",
            form=form,
            event=event
        )


def create_demo_values():
    """
    Initiate the DB : put fake data to simulate what the pages would look like
    """
    reservations = [
        ["12/01/22", "21/01/22", ReservationStatus.Ongoing, False, 1, 1],
        ["01/01/22", "22/01/22", ReservationStatus.Ongoing, True, 2, 0],
        ["12/01/22", None, ReservationStatus.Planned, False, 3, 1],
        ["30/12/21", "10/01/22", ReservationStatus.Completed, False, 1, 0],
    ]

    for resi in reservations:
        res = Reservation()
        res.collect_date = datetime.strptime(resi[0], "%d/%m/%y")
        if resi[1] != None:
            res.return_date = datetime.strptime(resi[1], "%d/%m/%y")
        res.status = resi[2]
        res.extended = resi[3]
        res.user_id = resi[4]
        res.event_id = resi[5]
        db.session.add(res)
        db.session.commit()
