# rivet-ui-viewer-kit

`rivet-ui-viewer-kit` packages a practical frontend apps exercise in Lua. The emphasis is on deterministic behavior, a small public API, and examples that explain the tradeoffs.

## How I Read Rivet UI Viewer Kit

The useful thing to inspect here is how the same score rule is represented in code, metadata, and examples. If those three pieces disagree, the audit script should make the drift visible.

## Problem Shape

The repository exists to keep a technical idea small enough to reason about. The implementation avoids external dependencies where possible, then uses fixtures to make changes easy to review.

## Scenario Walkthrough

The extended cases are not random smoke tests. `degraded` keeps pressure on the review path, while `surge` shows the model when capacity and weight are strong enough to clear the threshold.

## Internal Model

The design is intentionally direct: parse or construct a signal, score it, classify it, and verify the expected branch. This makes the repository useful for studying frontend apps behavior without needing a service or database unless the language project itself is SQL. The Lua project keeps the module shape simple and validates behavior through a direct script.

## Main Behaviors

- Models view models with deterministic scoring and explicit review decisions.
- Uses fixture data to keep interaction state changes visible in code review.
- Includes extended examples for layout checks, including `surge` and `degraded`.
- Documents fixture data tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.

## How To Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.

## Validation

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Repository Map

- `src`: primary implementation
- `tests`: verification harness
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands

## Follow-Up Work

- Split the scoring constants into a typed configuration object and validate it before use.
- Add a comparison mode that shows how decisions change when one signal is adjusted.
- Add a loader for `examples/extended_cases.csv` and promote selected cases into the language test suite.
- Add one more frontend apps fixture that focuses on a malformed or borderline input.

## Known Edges

The examples cover useful edges, not every edge. A larger version would add malformed-input tests, richer reports, and deeper domain parsers.

## Run It Locally

Clone the repository, enter the directory, and run the verifier. No database server, cloud account, or token is required.
