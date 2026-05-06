"""Executable checks for the rivet-ui-viewer-kit casebook."""

from __future__ import annotations

from collections import Counter

from . import rivet_ui_viewer_kit_segment_00
from . import rivet_ui_viewer_kit_segment_01
from . import rivet_ui_viewer_kit_segment_02
from . import rivet_ui_viewer_kit_segment_03
from . import rivet_ui_viewer_kit_segment_04
from . import rivet_ui_viewer_kit_segment_05
from . import rivet_ui_viewer_kit_segment_06
from . import rivet_ui_viewer_kit_segment_07
from . import rivet_ui_viewer_kit_segment_08
from . import rivet_ui_viewer_kit_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from rivet_ui_viewer_kit_segment_00.iter_rivet_ui_viewer_kit_00()
    yield from rivet_ui_viewer_kit_segment_01.iter_rivet_ui_viewer_kit_01()
    yield from rivet_ui_viewer_kit_segment_02.iter_rivet_ui_viewer_kit_02()
    yield from rivet_ui_viewer_kit_segment_03.iter_rivet_ui_viewer_kit_03()
    yield from rivet_ui_viewer_kit_segment_04.iter_rivet_ui_viewer_kit_04()
    yield from rivet_ui_viewer_kit_segment_05.iter_rivet_ui_viewer_kit_05()
    yield from rivet_ui_viewer_kit_segment_06.iter_rivet_ui_viewer_kit_06()
    yield from rivet_ui_viewer_kit_segment_07.iter_rivet_ui_viewer_kit_07()
    yield from rivet_ui_viewer_kit_segment_08.iter_rivet_ui_viewer_kit_08()
    yield from rivet_ui_viewer_kit_segment_09.iter_rivet_ui_viewer_kit_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def rivet_ui_viewer_kit_summary() -> dict:
    return assert_expected()
