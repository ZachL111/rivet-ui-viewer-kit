# Review Journal

The repository goal stays the same: develop a Lua command-oriented project for viewer scenarios with bounded scenario files, conflict explanations, and explicit failure cases. This note explains the added review angle.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its frontend apps focus without claiming live deployment or external usage.

## Cases

- `baseline`: `view drift`, score 193, lane `ship`
- `stress`: `state pressure`, score 205, lane `ship`
- `edge`: `layout risk`, score 130, lane `watch`
- `recovery`: `interaction cost`, score 183, lane `ship`
- `stale`: `view drift`, score 221, lane `ship`

## Note

A future change should add new cases before it changes the scoring rule.
