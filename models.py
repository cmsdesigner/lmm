import datetime
from flask import url_for
from extensions import db
from helpers import slugify
import json
from decimal import Decimal

from collections import OrderedDict


class DtiInfo(db.Model):
    __tablename__ = 'dti_info'

    id = db.Column(db.Integer, primary_key=True)
    cnt = db.Column(db.Integer)
    loan_amt = db.Column(db.Float)
    income = db.Column(db.Float)
    dti = db.Column(db.Float)
    max_dti = db.Column(db.Float)
    min_dti = db.Column(db.Float)
    std_dti = db.Column(db.Float)
    state_code = db.Column(db.Integer)
    county_code = db.Column(db.Integer)
    loan_type = db.Column(db.Integer)
    spread = db.Column(db.Float)

    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            attr = getattr(self, key)
            if isinstance(attr, Decimal):
                result[key] =  "%.2f" % attr
            else:
                result[key] = attr
        return result

    def __repr__(self):
        return '<DtiInfo %d %d %d>' % (self.state_code, self.county_code, self.loan_type)

class Zip(db.Model):
    __tablename__ = 'zips'

    id = db.Column(db.Integer, primary_key=True)
    zip = db.Column(db.String(5), unique=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    city = db.Column(db.String(30))
    state = db.Column(db.String(2))
    county = db.Column(db.String(30))
    zip_class = db.Column(db.String(30))
    msa = db.Column(db.Integer)
    pmsa = db.Column(db.Integer)
    county_fips = db.Column(db.Integer)
    state_fips = db.Column(db.Integer)

    def __repr__(self):
        return '<Zip %s %s,%s>' % (self.zip, self.city, self.state)

    def dti_info(self, loan_type):
        dti_info = DtiInfo.query.filter_by(state_code=self.state_fips)
        dti_info = dti_info.filter_by(county_code=self.county_fips)
        dti_info = dti_info.filter_by(loan_type=loan_type)
        return dti_info.first()

