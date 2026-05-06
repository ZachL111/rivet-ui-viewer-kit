# rivet-ui-viewer-kit

`rivet-ui-viewer-kit` is a Lua project in frontend apps. Its focus is to develop a Lua command-oriented project for viewer scenarios with bounded scenario files, conflict explanations, and explicit failure cases.

## Why I Keep It Small

The point is to make a small domain rule concrete enough that a reader can change it and immediately see what broke.

## Rivet UI Viewer Kit Review Notes

Start with `view drift` and `layout risk`. Those cases create the widest score spread in this repo, so they are the best quick check when the model changes.

## Included Behavior

- `fixtures/domain_review.csv` adds cases for view drift and state pressure.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/rivet-ui-viewer-walkthrough.md` walks through the case spread.
- The Lua code includes a review path for `view drift` and `layout risk`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Internal Model

The core code exposes a scoring path and the added review layer uses `signal`, `slack`, `drag`, and `confidence`. The domain terms are `view drift`, `state pressure`, `layout risk`, and `interaction cost`.

The Lua implementation avoids hidden state so fixture changes are easy to reason about.

## Try It Locally

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Validation

The same command runs the local verification path. The highest-scoring domain case is `stale` at 221, which lands in `ship`. The most cautious case is `edge` at 130, which lands in `watch`.

## Scope

The repository is intentionally scoped to local checks. I would expand it by adding adversarial fixtures before adding features.
