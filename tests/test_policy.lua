package.path = "src/?.lua;" .. package.path
local policy = require("policy")

local signal_case_1 = { demand = 60, capacity = 104, latency = 20, risk = 8, weight = 7 }
assert(policy.score(signal_case_1) == 153)
assert(policy.classify(signal_case_1) == "review")
local signal_case_2 = { demand = 59, capacity = 104, latency = 20, risk = 24, weight = 6 }
assert(policy.score(signal_case_2) == 84)
assert(policy.classify(signal_case_2) == "review")
local signal_case_3 = { demand = 85, capacity = 98, latency = 8, risk = 19, weight = 13 }
assert(policy.score(signal_case_3) == 207)
assert(policy.classify(signal_case_3) == "accept")
