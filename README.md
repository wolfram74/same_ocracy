# same_ocracy
bot_quality
  bot_id: int
  guesses: int
  correct: int

markov bot occasionally fails

figures table
  id
  handle
  name
impersonations table
  id
  figure_id
  guesses
  corrects

confusions table
  id
  source_figure_id
  other_figure_id
  guesses
  corrects

export APP_SETTINGS='config.DevelopmentConfig'
export DATABASE_URL='postgresql://localhost/sameocracy_dev'
