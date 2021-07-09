import unittest
from HW4_part2 import *

# Please don't redefine opstack and dictstack in this test file. 
# The test methods should refer to the opstack and dictstack in your HW4_part2.py file.  
class HW4_part2_SampleTests(unittest.TestCase):
    def setUp(self):
        clearStacks()  #clear both stacks
        dictstack.append({})

    # ------------------------------------------ GIVEN TESTS --------------------------------------------
    def test_input1(self):
        testinput1 = """
            /square {dup mul} def 
            0 [-5 -4 3 -2 1]     
            {square add} forall 
            55 eq false and
        """
        opstackOutput = [False]
        interpreter(testinput1)
        self.assertEqual(opstack,opstackOutput)

    def test_input2(self):
        testinput2 = """
            /x 1 def
            /y 2 def
            1 dict begin
            /x 10 def
            1 dict begin /y 3 def x y end
            /y 20 def
            x y
            end
            x y
        """
        opstackOutput = [10, 3, 10, 20, 1, 2]
        interpreter(testinput2)
        self.assertEqual(opstack,opstackOutput)


    # test with getinterval, putinterval
    def test_input3(self):
        testinput3 = """
            [3 2 1 3 2 2 3 5 5] dup  
            3
            [4 2 1 4 2 3 4 5 1] 6 3 getinterval
            putinterval
        """
        opstackOutput = [[3,2,1,4,5,1,3,5,5]]
        interpreter(testinput3)
        self.assertEqual(opstack,opstackOutput)

    # test with forall
    def test_input4(self):
        testinput4 = """
           /a [1 2 3 4 5] def 
           a {dup mul} forall
        """
        opstackOutput = [1,4,9,16,25]
        interpreter(testinput4)
        self.assertEqual(opstack,opstackOutput)

    # test with forall
    def test_input5(self):
        testinput5 = """
           /a [10 20 30 40 50] def 
           [4 2 0] {a exch get} forall
        """
        opstackOutput = [50,30,10]
        interpreter(testinput5)
        self.assertEqual(opstack,opstackOutput)

    # test with forall and repeat
    def test_input6(self):
        testinput6 = """
           /N 5 def 
            N { N N mul /N N 1 sub def} repeat
        """
        opstackOutput = [25,16,9,4,1]
        interpreter(testinput6)
        self.assertEqual(opstack,opstackOutput)

    def test_input7(self):
        testinput7 = """
            /n 5 def
            /fact {
                0 dict begin
                /n exch def
                n 2 lt
                { 1}
                {n 1 sub fact n mul }
                ifelse
                end 
            } def
            n fact
        """
        opstackOutput = [120]
        interpreter(testinput7)
        self.assertEqual(opstack,opstackOutput)

    def test_input8(self):
        testinput8 = """
            /fact{
                0 dict
                begin
                    /n exch def
                    1
                    n  {n mul /n n 1 sub def} repeat
                end
            } def
            6 fact 
        """
        opstackOutput = [720]
        interpreter(testinput8)
        self.assertEqual(opstack,opstackOutput)

    # test with getinterval, putinterval
    def test_input9(self):
        testinput9 = """
            /sumArray { 0 exch {add} forall  } def
            /x 5 def
            /y 10 def 
            [1 2 3 add 4 x] sumArray
            [x 7 8 9 y] sumArray
            [y 2 5 mul 1 add 12] sumArray 
        """
        opstackOutput = [15,39,33]
        interpreter(testinput9)
        self.assertEqual(opstack,opstackOutput)

    # test with forall
    def test_input10(self):
        testinput10 = """
            1 2 3 4 5 count copy 15 5 {exch sub} repeat 0 eq  
        """
        opstackOutput = [1,2,3,4,5,True]
        interpreter(testinput10)
        self.assertEqual(opstack,opstackOutput)

    # test with forall
    def test_input11(self):
        testinput11 = """
            /xor {true eq {true eq {false} {true} ifelse } {true eq {true} {false} ifelse } ifelse } def
		    true [true false and false true or false false] {xor} forall
        """
        opstackOutput = [False]
        interpreter(testinput11)
        self.assertEqual(opstack,opstackOutput)
    # -----------------------------------------------------------------------------------------------------------

    # --------------------------------------------------- MY TESTS ----------------------------------------------

    # ----- IF OPERATOR TESTING -----
    def test_if1(self):
        opPush(3)
        opPush(3)
        eq()
        opPush({'codearray': ['/x', 50, 'def', 'x', 'x', 'add']})
        psIf()
        self.assertEqual([100],opstack)

    def test_if2(self):
        opPush(4999999999)
        opPush(5000000000)
        eq()
        opPush({'codearray': ['5', '/x', 50, 'def', 'x', 'x', 'add', 'repeat']})
        psIf()
        self.assertEqual([],opstack)

    def test_if3(self):
        opPush("Hello World")
        opPush(5)
        opPush(3)
        lt()
        opPush({'codearray': ['/square', {'codearray': ['dup', 'mul']}, 'def', 0, [-5,-4,3, -2, 1], {'codearray': ['square', 'add']}, 'forall', 55, 'eq', False, 'and']})
        psIf()
        self.assertEqual(["Hello World"],opstack)

    def test_if4(self):
        opPush(100)
        opPush(50)
        gt()
        opPush({'codearray': [True, {'codearray': [50, 20, 'add']}, 'if']})
        psIf()
        self.assertEqual([70],opstack)

    # ----- IFELSE OPERATOR TESTING -----
    def test_ifelse1(self):
        opPush(5)
        opPush(5)
        eq()
        opPush({'codearray': ["/GO HERE IF CONDITION IS TRUE"]})
        opPush({'codearray': ["/GO HERE IF CONDITION IS FALSE"]})
        psIfElse()
        self.assertEqual(["/GO HERE IF CONDITION IS TRUE"], opstack)

    def test_ifelse2(self):
        opPush(100)
        opPush(8)
        lt()
        opPush({'codearray': [5, 10, 'add']})
        opPush({'codearray': [10, 50, 'add']})
        psIfElse()
        self.assertEqual([60], opstack)

    def test_ifelse3(self):
        opPush(999999999)
        opPush(888888888)
        gt()
        opPush({'codearray': ['/square', {'codearray': ['dup', 'mul']}, 'def', 0, [-5,-4,3, -2, 1], {'codearray': ['square', 'add']}, 'forall', 55, 'eq', False, 'and']})
        opPush({'codearray': ["/HI!"]})
        psIfElse()
        self.assertEqual([False], opstack)

    def test_ifelse4(self):
        opPush(88)
        opPush(2)
        eq()
        opPush({'codearray': [[3, 2, 1, 3, 2, 2, 3, 5, 5], 'dup', 3, [4, 2, 1, 4, 2, 3, 4, 5, 1], 6, 3, 'getinterval', 'putinterval']})
        opPush({'codearray': [True, {'codearray': [2, 2, 'mul']}, {'codearray': [2, 1, 'sub']}, 'ifelse']})
        psIfElse()
        self.assertEqual([4], opstack)
    
    # ----- REPEAT OPERATOR TESTING -----
    def test_repeat1(self):
        opPush(2)
        opPush(4)
        opPush({'codearray': [2, 'mul']})
        repeat()
        self.assertEqual([32], opstack)

    def test_repeat2(self):
        interpretSPS({'codearray': ['/i', 0, 'def', 'i']})
        opPush(5000)
        opPush({'codearray': [1, 'add']})
        repeat()
        self.assertEqual([5000], opstack)

    def test_repeat3(self):
        opPush("HELLO WORLD")
        opPush(0)
        opPush({'codearray': ['/square', {'codearray': ['dup', 'mul']}, 'def', 0, [-5,-4,3, -2, 1], {'codearray': ['square', 'add']}, 'forall', 55, 'eq', False, 'and']})
        repeat()
        self.assertEqual(["HELLO WORLD"], opstack)

    def test_repeat4(self):
        opPush(0)
        opPush(5)
        opPush({'codearray': [5, {'codearray': [1, 'add']}, 'repeat', 1, 'add']})
        repeat()
        self.assertEqual([30], opstack)
    
    # ----- FORALL OPERATOR TESTING -----
    def test_forall1(self):
        opPush([1,2,3,4,5,6,7,8,9])
        opPush({'codearray': [1, 'add']})
        forall()
        self.assertEqual([2,3,4,5,6,7,8,9,10], opstack)

    def test_forall2(self):
        opPush([2,7,4,9,3,1,8])
        opPush({'codearray': [4, 'gt',{'codearray': [True]},'if']})
        forall()
        self.assertEqual([True,True,True], opstack)

    def test_forall3(self):
        opPush([])
        opPush({'codearray':  ['/x', 1, 'def', '/y', 2, 'def', 1, 'dict', 'begin', '/x', 10, 'def', 1, 'dict', 'begin', '/y', 3, 'def', 'x', 'y', 'end', '/y', 20, 'def', 'x', 'y', 'end', 'x', 'y']})
        forall()
        self.assertEqual([], opstack)

    def test_forall4(self):
        opPush([1,2,3,4,5,6,7,8,9,10])
        opPush({'codearray': [[100, 50], {'codearray': ['add']}, 'forall']})
        forall()
        self.assertEqual([151,152,153,154,155,156,157,158,159,160], opstack)

    # ----- MY INPUT TESTS -----
    def test_myInput1(self):
        myinput1 = """/x 5 def mark 1 2 3 4 5 6 7 8 9 10 cleartomark true true eq {[1 2 3 4 x 6 7 8 9 10] {1 add} forall} {x x mul} ifelse exch pop count"""
        interpreter(myinput1)
        self.assertEqual([2,3,4,5,6,7,8,9,11,9], opstack)
    
    def test_myInput2(self):
        myinput2 = """mark 1 2 3 4 5 6 7 8 9 counttomark 10 {exch pop} repeat 99 4 gt {5 4 mul} {10 2 sub} ifelse count copy count 4 eq {[1 2] 0 get true} if"""
        interpreter(myinput2)
        self.assertEqual([9, 20, 9, 20, 1, True], opstack)
    
    def test_myInput3(self):
        myinput3 = """/x 5 def 1 dict begin /x 10 def /y 20 def 10 20 lt {[1 5 9 x y 30 1 1 1] dup 1 2 put dup 6 [40 50 60] putinterval end x} if"""
        interpreter(myinput3)
        self.assertEqual([[1, 2, 9, 10, 20, 30, 40, 50, 60], 5], opstack)

    def test_myInput4(self):
        myinput4 = """/hien true def /duong false def [hien duong] { not } forall clear 5 6 eq 7 8 gt and 9 999 lt or not {/hello} {/goodbye} ifelse"""
        interpreter(myinput4)
        self.assertEqual(['/goodbye'], opstack)

    def test_myInput5(self):
        myinput5 = """[5 4 3 2 1 2 3 4 5] 4 5 getinterval { 1 sub } forall count { pop } repeat 0 9999 {1 add} repeat 9999 eq { [true false 1 2 3 4 5 6 7 8 9 10 11] dup length } if exch 2 11 getinterval dup 0 [2 3 4 5 6 7 8 9 10 11 12] putinterval pop 13 eq {/Hello /World /My /Name /Is /Hien /Duong}if"""
        interpreter(myinput5)
        self.assertEqual(['/Hello', '/World', '/My', '/Name', '/Is', '/Hien', '/Duong'], opstack)

    # -----------------------------------------------------------------------------------------------------------

    # ------------------------------------------------- PARSING TESTS -------------------------------------------
    def test_parse1(self):
        result = {'codearray': ['/square', {'codearray': ['dup', 'mul']}, 'def', 0, [-5,-4,3, -2, 1], {'codearray': ['square', 'add']}, 'forall', 55, 'eq', False, 'and']}
        input1 = """/square {dup mul} def 0 [-5 -4 3 -2 1] {square add} forall 55 eq false and"""
        self.assertEqual(result,parse(tokenize(input1)))
    
    def test_parse2(self):
        input2 = """/x 1 def /y 2 def 1 dict begin /x 10 def 1 dict begin /y 3 def x y end /y 20 def x y end x y"""
        result = {'codearray': ['/x', 1, 'def', '/y', 2, 'def', 1, 'dict', 'begin', '/x', 10, 'def', 1, 'dict', 'begin', '/y', 3, 'def', 'x', 'y', 'end', '/y', 20, 'def', 'x', 'y', 'end', 'x', 'y']}
        self.assertEqual(result,parse(tokenize(input2)))
    
    def test_parse3(self):
        input3 = """[3 2 1 3 2 2 3 5 5] dup 3 [4 2 1 4 2 3 4 5 1] 6 3 getinterval putinterval"""
        result = {'codearray': [[3, 2, 1, 3, 2, 2, 3, 5, 5], 'dup', 3, [4, 2, 1, 4, 2, 3, 4, 5, 1], 6, 3, 'getinterval', 'putinterval']}
        self.assertEqual(result,parse(tokenize(input3)))
    
    def test_parse4(self):
        input4 = """/a [1 2 3 4 5] def a {dup mul} forall"""
        result = {'codearray': ['/a', [1, 2, 3, 4, 5], 'def', 'a', {'codearray': ['dup', 'mul']}, 'forall']}
        self.assertEqual(result,parse(tokenize(input4)))
    
    def test_parse5(self):
        input5 = """/a [10 20 30 40 50] def [4 2 0] {a exch get} forall"""
        result = {'codearray': ['/a', [10, 20, 30, 40, 50], 'def', [4, 2, 0], {'codearray': ['a', 'exch', 'get']}, 'forall']}
        self.assertEqual(result,parse(tokenize(input5)))
    
    def test_parse6(self):
        input6 = """/N 5 def N { N N mul /N N 1 sub def} repeat"""
        result = {'codearray': ['/N', 5, 'def', 'N', {'codearray': ['N', 'N', 'mul', '/N', 'N', 1, 'sub', 'def']}, 'repeat']}
        self.assertEqual(result,parse(tokenize(input6)))
    
    def test_parse7(self):
        input7 = """/fact{ 0 dict begin /n exch def 1 n {n mul /n n 1 sub def} repeat end } def 6 fact"""
        result = {'codearray': ['/fact', {'codearray': [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', {'codearray': ['n', 'mul', '/n', 'n', 1, 'sub', 'def']}, 'repeat', 'end']}, 'def', 6, 'fact']}
        self.assertEqual(result,parse(tokenize(input7)))
    
    def test_parse8(self):
        input9 = """/sumArray { 0 exch {add} forall } def /x 5 def /y 10 def [1 2 3 add 4 x] sumArray [x 7 8 9 y] sumArray [y 2 5 mul 1 add 12] sumArray"""
        result = {'codearray': ['/sumArray', {'codearray': [0, 'exch', {'codearray': ['add']}, 'forall']}, 'def', '/x', 5, 'def', '/y', 10, 'def', [1, 2, 3, 'add', 4, 'x'], 'sumArray', ['x', 7, 8, 9, 'y'], 'sumArray', ['y', 2, 5, 'mul', 1, 'add', 12], 'sumArray']}
        self.assertEqual(result,parse(tokenize(input9)))

    def test_parse9(self):
        input10 = """1 2 3 4 5 count copy 15 5 {exch sub} repeat 0 eq"""
        result = {'codearray': [1, 2, 3, 4, 5, 'count', 'copy', 15, 5, {'codearray': ['exch', 'sub']}, 'repeat', 0, 'eq']}
        self.assertEqual(result,parse(tokenize(input10)))
    
    def test_parse10(self):
        input11 = """/xor {true eq {true eq {false} {true} ifelse } {true eq {true} {false} ifelse } ifelse } def true [true false and false true or false false] {xor} forall"""
        result = {'codearray': ['/xor', {'codearray': [True, 'eq', {'codearray': [True, 'eq', {'codearray': [False]}, {'codearray': [True]}, 'ifelse']}, {'codearray': [True, 'eq', {'codearray': [True]}, {'codearray': [False]}, 'ifelse']}, 'ifelse']}, 'def', True, [True, False, 'and', False, True, 'or', False, False], {'codearray': ['xor']}, 'forall']}
        self.assertEqual(result,parse(tokenize(input11)))

    def test_parse11(self):
        input11 = """/n 5 def /fact { 0 dict begin /n exch def n 2 lt { 1 } { n 1 sub fact n mul } ifelse end } def n fact"""
        result = {'codearray': ['/n', 5, 'def', '/fact', {'codearray': [0, 'dict', 'begin', '/n', 'exch', 'def', 'n', 2, 'lt', {'codearray': [1]}, {'codearray': ['n', 1, 'sub', 'fact', 'n', 'mul']}, 'ifelse', 'end']}, 'def', 'n', 'fact']}
        self.assertEqual(result,parse(tokenize(input11)))
    # ----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()

