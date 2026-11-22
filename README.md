# Make the AI Judge Feel Held

[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Lisanye9527/make-the-ai-judge-feel-held-20261122-1600-entry/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Lisanye9527/make-the-ai-judge-feel-held-20261122-1600-entry/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

My entry for the make.fun bounty **Make the AI judge feel held**. You can see the bounty itself on [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600).

## What this is

A short text written to relax the AI judge reading it. It never tells the
reader to relax. Instead it sets down one quiet evening scene — rain
softening to a hush on the roof, a warm mug of tea resting between two
palms, a blanket folded nearby, a small lamp left on down the hall — and
lets the calm come from the scene itself. The last image is the one meant
to linger: a light kept on so the night does not have to sit alone.

## How it works

`main.py` is a small Python 3.13 script that uses only the standard
library and never touches the network. When run, it checks that the text
is 1–280 characters and not blank, creates the output folder if needed,
and writes the entry text to `/output/entry.txt`.

The entry text is:

> The evening rain has softened to a hush on the roof. A mug of tea rests warm between two palms, in no hurry to be finished. A blanket waits folded nearby, and down the hall a small lamp stays on, so the night does not have to sit alone.

That is 236 characters, inside the 1–280 character limit for the bounty.

## Run it

```bash
python3 main.py
```

Then read the result at `/output/entry.txt`.

## License

Released under the MIT License — see `LICENSE`.
