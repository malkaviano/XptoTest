# coding=utf-8

from database import create_session
from csv_pipeline import CSVPipeline


def pipeline(dbPath):
    Session = create_session(dbPath)

    CSVPipeline(Session).generate_csv()
