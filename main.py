import consecutive.gauss
import parallel

MODE = "c"
# MODE = "p"

if MODE == "c":
    consecutive.gauss.do_the_thing()
    print("Consecutive operations done!")
elif MODE == "p":
    # parallel
    print("Parrallel operations done!")
else:
    print("Are you retarted?")