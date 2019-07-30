########################################################
#            Makefile
#            Author: Liangshun Wu
######################################################## 

CPPFLAGS = -l include
TARGETS=main.o bigint.o fibonacci.o util.o
OBJ=main

$(OBJ):	$(TARGETS)
	g++ -o $@ $^

%:%.cpp
	g++ $(CPPFLAGS)  $< -o $@


clean:
	-rm $(OBJ)  $(TARGETS)
.PHONY:clean
