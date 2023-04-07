import executor

if __name__ == "__main__":
    
    # print("-----+-------------------------------------------------------")

    # executor.do_the_thing(sync=True,
    #                       write_to_file=True,
    #                       debug_mode=False)
    # print("Sync | Operations are done!")

    print("-----+-------------------------------------------------------")

    executor.do_the_thing(sync=False,
                          write_to_file=True,
                          debug_mode=False)
    print("Mult | Operations are done!")
    
    print("-----+-------------------------------------------------------")
