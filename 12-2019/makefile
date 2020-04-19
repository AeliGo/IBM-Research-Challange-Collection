VPATH = ./:../utils:../utils/math

app:integrate.o math.o
	gcc -o app integrate.o math.o && ./app
integrate.o:integrate.c math.h
	gcc -c integrate.c
math.o:math.c
	gcc -c ../utils/math/math.c
clean:
	rm app integrate.o math.o

