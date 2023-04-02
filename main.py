import consecutive.executor
# import parallel.executor

MODE = "c"
# MODE = "p"

if MODE == "c":
    consecutive.executor.do_the_thing(True)
    print("C | Operations are done!")
elif MODE == "p":
    # parallel.executor.do_the_thing()
    print("P | Operations are done!")
else:
    print("? | Are you retarted?")