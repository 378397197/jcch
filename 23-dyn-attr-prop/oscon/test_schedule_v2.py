import pytest

import schedule_v2 as schedule

@pytest.yield_fixture
def records():
    yield schedule.load(schedule.JSON_PATH)


def test_load(records):
    assert len(records) == 895


def test_record_attr_access():
    rec = schedule.Record(spam=99, eggs=12)
    assert rec.spam == 99
    assert rec.eggs == 12


def test_venue_record(records):
    venue = records['venue.1469']
    assert venue.serial == 1469
    assert venue.name == 'Exhibit Hall C'


def test_fetch_speaker_record():
    speaker = schedule.Record.fetch('speaker.3471')
    assert speaker.name == 'Anna Martelli Ravenscroft'


def test_event_type():
    event = schedule.Record.fetch('event.33950')
    assert type(event) is schedule.Event
    assert repr(event) == "<Event 'There *Will* Be Bugs'>"


def test_event_repr():
    event = schedule.Record.fetch('event.33950')
    assert repr(event) == "<Event 'There *Will* Be Bugs'>"
    event2 = schedule.Event(serial=77, kind='show')
    assert repr(event2) == '<Event serial=77>'


def test_event_venue():
    event = schedule.Record.fetch('event.33950')
    assert event.venue_serial == 1449
    assert event.venue == schedule.Record.fetch('venue.1449')
    assert event.venue.name == 'Portland 251'
