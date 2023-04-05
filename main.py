import executor

if __name__ == "__main__":
    executor.do_the_thing(sync=True,
                          write_to_file=True,
                          debug_mode=False)
    print("S | Operations are done!")

    executor.do_the_thing(sync=False,
                          write_to_file=True,
                          debug_mode=False)
    print("M | Operations are done!")