'use strict'

const handler = require('./index')

module.exports = async (event, context) => {
  return handler(event)
}
