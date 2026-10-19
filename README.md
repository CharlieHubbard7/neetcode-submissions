# NeetCode & LeetCode Solutions — @CharlieHubbard7

> My solutions to coding interview problems, synced automatically from [NeetCode.io](https://neetcode.io) and [LeetCode](https://leetcode.com).

---

## What is this?

This repository collects my accepted solutions from two platforms:

- **[NeetCode.io](https://neetcode.io)** — curated interview problems with video explanations. Synced with NeetCode's built-in **GitHub Sync** feature.
- **[LeetCode](https://leetcode.com)** — the classic problem bank. Synced with the [LeetSync](https://github.com/LeetSync/LeetSync) browser extension.

---

## Repository structure

```
.
├── Data Structures & Algorithms/   ← NeetCode solutions (by topic)
│   └── <problem-id>/
│       ├── submission-0.<ext>
│       └── submission-1.<ext>
└── LeetCode/                       ← LeetCode solutions
    └── <number>-<problem-slug>/
        ├── README.md               ← problem statement
        └── <problem-slug>.<ext>    ← solution
```

### NeetCode

Solutions are organized by topic folder, then problem ID. Each submission is stored as a separate file:

```
Data Structures & Algorithms/two-integer-sum/submission-0.py
Data Structures & Algorithms/binary-search/submission-1.py
```

### LeetCode

Each problem gets its own folder named `<number>-<slug>`, containing the problem description and my solution:

```
LeetCode/35-search-insert-position/README.md
LeetCode/35-search-insert-position/search-insert-position.py
```

---

## How syncing works

### NeetCode → GitHub Sync

1. Connect GitHub at [neetcode.io/profile/github](https://neetcode.io/profile/github).
2. **Auto-commit** — every submission is pushed here automatically (configurable by status).
3. **Bulk Sync** — push all past solutions at once.
4. **Manual sync** — sync or remove individual submissions from a problem's submission history.

### LeetCode → LeetSync

1. Install the LeetSync extension and connect it to this repository.
2. Every accepted LeetCode submission is committed with its runtime and memory stats, e.g.
   `Time: 0 ms (100.00%) | Memory: 19.7 MB (96.04%) - LeetSync`.

---

## Languages

| Language | Extension |
|---|---|
| Python | `.py` |
| JavaScript | `.js` |
| TypeScript | `.ts` |
| Java | `.java` |
| C++ | `.cpp` |
| C# | `.cs` |
| Go | `.go` |
| Rust | `.rs` |
| Kotlin | `.kt` |
| Swift | `.swift` |
| SQL | `.sql` |
