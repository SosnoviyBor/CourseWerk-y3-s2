import executor

if __name__ == "__main__":
    
    print("--+-----------------------------------------")

    executor.do_the_thing(sync=True,
                          write_to_file=False,
                          debug_mode=False)
    print("S | Operations are done!")

    print("--+-----------------------------------------")

    executor.do_the_thing(sync=False,
                          write_to_file=False,
                          debug_mode=False)
    print("M | Operations are done!")
    
    print("--+-----------------------------------------")
