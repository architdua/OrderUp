# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
from datetime import datetime, timedelta
from twilio.rest import TwilioRestClient
from gluon import utils as gluon_utils

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """

    return dict()

def order():
    orderform = SQLFORM(db.request)
    query=((db.request.author == auth.user_id))
    fields = (db.request.id, db.request.name, db.request.toName,
              db.request.toNumber, db.request.meal, db.request.rice,
              db.request.beans, db.request.meat, db.request.salsa,
              db.request.guac, db.request.corn, db.request.sourcream,
              db.request.cheese, db.request.lettuce, db.request.drink,
              db.request.chips)
    headers = {'request.id':   'ID',
           'request.name': 'Your Name',
           'request.toName': 'Friends Name',
           'request.toNumber': 'Number',
           'request.meal': 'Meal Type',
           'request.rice': 'Rice',
           'request.beans': 'Beans',
            'request.meat': 'Meat/Veggies',
            'request.salsa': 'Salsa',
            'request.guac': 'Guacamole',
            'request.corn': 'Corn',
            'request.sourcream': 'Sour Cream',
            'request.cheese': 'Cheese',
            'request.lettuce': 'Lettuce',
            'request.drink': 'Drink',
            'request.chips': 'Chips'
           }
    links = [lambda row: A('Use this',_href=URL("default","addpass",args=[row.id]))]
    gridform = SQLFORM.grid(query=query, fields=fields, headers=headers, links=links,
                create=False, deletable=False, editable=False, maxtextlength=64, paginate=25)
  
    if orderform.process().accepted:
        it = "OrderUp!: Hi " +orderform.vars.toName+", " +orderform.vars.name+ " sent you this order: " + orderform.vars.meal + " with " + orderform.vars.rice + ", " + orderform.vars.beans + " beans, " + orderform.vars.meat + ", " + orderform.vars.salsa + ", " +orderform.vars.guac+ ", " +orderform.vars.corn+ ", " +orderform.vars.sourcream+ ", " +orderform.vars.cheese+ ", " +orderform.vars.lettuce+ ", " +orderform.vars.drink+ ", " +orderform.vars.chips

        sid = "ACab534576d2a1f014c3e439d52fc1a852"
        token = "f94725304eee947ea4d92aba1fe902fd"
        client = TwilioRestClient(sid, token)
        client.messages.create(
            to="+1" + orderform.vars.toNumber,
            from_="+16506035269",
            body=it
        )
        redirect(URL('default','index'))

    return dict(orderform=orderform, gridform=gridform, _next=dict(_next=request.url))

def addpass():
    orderform = SQLFORM(db.request)
    order_id = (request.args(0))
    order = db((db.request.id == order_id))
    order = order.select().first()
    orderform.vars.toName = order['toName']
    orderform.vars.name = order['name']
    orderform.vars.toNumber = order['toNumber']
    orderform.vars.meal = order['meal']
    orderform.vars.beans = order['beans']
    orderform.vars.rice = order['rice']
    orderform.vars.meat = order['meat']
    orderform.vars.salsa = order['salsa']
    orderform.vars.guac = order['guac']
    orderform.vars.corn = order['corn']
    orderform.vars.sourcream = order['sourcream']
    orderform.vars.cheese = order['cheese']
    orderform.vars.lettuce = order['lettuce']
    orderform.vars.drink = order['drink']
    orderform.vars.chips = order['chips']

    if orderform.process().accepted:
        it = "OrderUp!: Hi " +orderform.vars.toName+", " +orderform.vars.name+ " sent you this order: " + orderform.vars.meal + " with " + orderform.vars.rice + ", " + orderform.vars.beans + " beans, " + orderform.vars.meat + ", " + orderform.vars.salsa + ", " +orderform.vars.guac+ ", " +orderform.vars.corn+ ", " +orderform.vars.sourcream+ ", " +orderform.vars.cheese+ ", " +orderform.vars.lettuce+ ", " +orderform.vars.drink+ ", " +orderform.vars.chips

        sid = "ACab534576d2a1f014c3e439d52fc1a852"
        token = "f94725304eee947ea4d92aba1fe902fd"
        client = TwilioRestClient(sid, token)
        client.messages.create(
            to="+1" + orderform.vars.toNumber,
            from_="+16506035269",
            body=it
        )
        redirect(URL('default','index'))

    #db.request.toName.default = request.get_vars.toName
    return dict(orderform=orderform, msg=T('Success! Your order went through'))

def contacts():
    """
    Create board.
    """
    draft_id = gluon_utils.web2py_uuid()
    return dict(draft_id=draft_id)

@auth.requires_signature()
def add_msg():
    db.contacts.update_or_insert((db.contacts.contact_id == request.vars.contact_id),
                            contact_id=request.vars.contact_id,
                            name=request.vars.name,
                            user_id = auth.user_id
                            )
    return "ok"


def load_messages():
    """Loads all messages for the user."""
    # rows = db(db.bds.author == auth.user_id).select()
    rows = db(db.contacts).select()
    d = {r.contact_id: {'name': r.name}
         for r in rows}
    return response.json(dict(board_dict=d))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

