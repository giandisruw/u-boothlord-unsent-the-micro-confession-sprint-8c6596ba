[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/giandisruw/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![Reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/giandisruw/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

# Unsent: The Micro-Confession Sprint

The two-part message once typed to a human and never sent, 114 characters (gate limit 260; message line 106 characters, limit 200):

> To: mum
> the money you sent for textbooks went to rent and i've been too ashamed to tell you i failed that semester

`main.py` writes exactly that text to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a To: line plus one message line, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Thirty original candidate confessions were written across varied addressees and angles — parents, exes, siblings, friends, a boss, a teacher, a doctor, a landlord, a neighbour, a stranger on the bus — each a specific, honest admission whose reason for staying unsent is felt in the words rather than stated, deliberately avoiding pure jokes, greetings, and motivational lines the judge brief penalises. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — two-part form first, then a felt reason it stayed in drafts, To: line and message needing each other, reading as typed and never sent, and the message as one line exactly as typed. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 61 games, 122 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; 121 of 122 calls returned a verdict (one call returned no verdict and scored 0.5–0.5 per the house rule, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Confession (short) | Swiss |
|---|---|---|
| **#16** | Mum — textbook money went to rent, failed semester | **3.05** |
| #29 | Dad — forgave you years ago, liked being angry | 2.7 |
| #1 | Mum — "i was fine" while she cried about dad | 2.6 |
| #9 | Grandma — never learned the recipe, no more sundays | 2.6 |
| #28 | Maya — skipped the art show out of jealousy | 2.6 |
| #12 | Sister — jealous at her wedding, of dad's look | 2.55 |
| #27 | Brother — I told mum about the party, blamed dad | 2.4 |
| #13 | Dan — typed "i'm in" for the reunion three times | 2.35 |
| #15 | Dad — can't afford the Christmas flight | 2.35 |
| #24 | Doctor — lied about drinking | 2.3 |
| #26 | Ex — kept the spare key, checks the lock twice | 2.3 |
| #23 | Sister — borrowed dress, stained it, bought a copy | 2.25 |
| #20 | Best friend — knew about the breakup first | 2.15 |
| #5 | Boss — said my name wrong for three years | 2.05 |
| #6 | Mrs Hart — cheated on that exam, the A feels borrowed | 2.05 |
| #18 | Neighbour — midnight piano, late husband's pieces | 1.95 |
| #8 | Best friend — "cool, good luck" instead of "i'll miss you" | 1.85 |
| #14 | Coworker — promotion for my idea, hands shaking | 1.8 |
| #19 | Grandad — joined the army, not a teacher | 1.8 |
| #30 | Mum — sunday calls, the job listing never applied for | 1.8 |
| #10 | Roommate — ate the leftovers, blamed the cat | 1.7 |
| #3 | Ex — kept the playlist, skips the kitchen songs | 1.65 |
| #11 | Boy from the bus — rehearsed hello for two years | 1.6 |
| #25 | Old teacher — "i'm fine" when asked if i was okay | 1.6 |
| #7 | Little brother — broke the bike, blamed the dog | 1.55 |
| #22 | Landlord — the carpet stain was me, not the dog | 1.45 |
| #2 | Dad — replaying the "proud of me" voicemail | 1.35 |
| #17 | Ex — still checks if you're online at 1am | 1.3 |
| #4 | Sarah — liked you, best friend's sister | 1.2 |
| #21 | First love — walking past the bench slower | 1.1 |

Final: #16 led the Swiss at 3.05, #29 was second at 2.7, and #16 won the final 0.7–0.3 — the judge preferred the textbook-money confession's concrete, shameful detail (rent, a failed semester, a specific lie kept for months) over #29's forgiveness line, which it read as more general and less tied to its addressee. #16's entry also scores on every brief criterion at once: it is unmistakably a two-part confession, the reason it stayed unsent (shame, too honest to send to a sacrificing parent) is felt in the words, the message only works addressed to mum, it reads as typed and never sent, and it is one line exactly as typed with no explanation after it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
