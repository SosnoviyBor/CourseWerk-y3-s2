import executor

MODE = "s"
# MODE = "m"

if __name__ == "__main__":
    if MODE == "s":
        executor.do_the_thing(sync=True,
                              write_to_file=True,
                              debug_mode=False)
        print("S | Operations are done!")

    elif MODE == "m":
        executor.do_the_thing(sync=False,
                              write_to_file=False,
                              debug_mode=True)
        print("M | Operations are done!")

    else:
        print("? | Are you retarted?")