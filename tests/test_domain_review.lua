package.path = "src/?.lua;" .. package.path
local review = require("domain_review")

local item = { signal = 56, slack = 36, drag = 13, confidence = 84 }
assert(review.score(item) == 193)
assert(review.lane(item) == "ship")
