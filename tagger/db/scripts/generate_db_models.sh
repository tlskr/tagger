#!/bin/sh

# Generate SqlAlchemy models from database schema

TABLE=$1
OUTFILE=$2

sqlacodegen postgresql://exerciser:password@localhost/blue_bite --tables $TABLE --outfile $OUTFILE

