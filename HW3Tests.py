import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        pass
    def test_sumSales(self):
        salesLog= {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}
        summedLog = {'Fri': 30, 'Mon': 80, 'Sat': 220, 'Thu': 80, 'Tue': 180, 'Wed': 225}
        self.assertDictEqual(sumSales(salesLog),summedLog)

    # ----------- MY TEST CASES FOR sumSales ----------------
    # edge case
    def test_sumSalesEdge(self):
        salesLog= {}
        summedLog = {}
        self.assertDictEqual(sumSales(salesLog),summedLog)
    
    #boundary cases
    def test_sumSalesBoundary1(self):
        salesLog= {'Amazon':{'Mon':0,'Wed':50},'Etsy':{'Mon':-1,'Fri':9223372036854775807}}
        summedLog = {'Fri': 9223372036854775807, 'Mon': -1, 'Wed': 50}
        self.assertDictEqual(sumSales(salesLog),summedLog)

    def test_sumSalesBoundary2(self):
        salesLog= {'Amazon':{'Mon':-9223372036854775807,'Tue':50},'Etsy':{'Tue':3000},'Petco':{'Tue':1000},'Costo':{'Tue':-50}}
        summedLog = {'Mon': -9223372036854775807, 'Tue': 4000}
        self.assertDictEqual(sumSales(salesLog),summedLog)  
    # -----------------------------------------------------------

    def test_sumSalesN(self):
        salesLogN = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN = {'Fri': 135,'Mon':245,'Sat':285,'Sun': 88,'Thu': 120,'Tue':180,'Wed':225}
        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)
    
    # ------------- MY TEST CASES FOR sumSalesN -----------------
    # edge case
    def test_sumSalesNEdge(self):
        salesLogN = [{}]
        summedLogN = {}
        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)

    # boundary cases
    def test_sumSalesNBoundary1(self):
        salesLogN = [{'Amazon':{'Mon':-216,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':-9223372036854775807},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN = {'Fri': 135,'Mon':-1,'Sat':285,'Sun': -9223372036854775807,'Thu': 120,'Tue':180,'Wed':225}
        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)

    def test_sumSalesNBoundary2(self):
        salesLogN = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':9223372036854775807},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN = {'Fri': 135,'Mon':245,'Sat':285,'Sun': 9223372036854775807,'Thu': 120,'Tue':180,'Wed':225}
        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)
    # -----------------------------------------------------------

    def test_searchDicts(self):
        #searchDicts inputs
        dictList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.assertEqual(searchDicts(dictList,"x"),2)
        self.assertEqual(searchDicts(dictList,"y"),False)
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"t"),None)

    # ------------ MY TEST CASES FOR searchDicts -------------
    # edge case
    def test_searchDictsEdge(self):
        #searchDicts inputs
        dictList = [{}]
        self.assertEqual(searchDicts(dictList,"x"),None)
        self.assertEqual(searchDicts(dictList,"y"),None)
        self.assertEqual(searchDicts(dictList,"z"),None)
        self.assertEqual(searchDicts(dictList,"t"),None)
    
    # boundary cases
    def test_searchDictsBoundary1(self):
        #searchDicts inputs
        dictList = [{"hello world":1,"y":True,"z":"found"},{"hello world": 9223372036854775807},{"y":False}]
        self.assertEqual(searchDicts(dictList,"hello world"), 9223372036854775807)

    def test_searchDictsBoundary2(self):
        #searchDicts inputs
        dictList = [{"hello world":1,"y":True,"z":{5:"ok lol"}},{"hello world": -9223372036854775807},{"y": (1,2)}]
        self.assertEqual(searchDicts(dictList,"hello world"), -9223372036854775807)
        self.assertEqual(searchDicts(dictList,"y"), (1,2)) 
        self.assertEqual(searchDicts(dictList,"z"), {5:"ok lol"}) 
    # --------------------------------------------------------------

    def test_searchDicts2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        self.assertEqual(searchDicts2(dictList2,"x"),1)
        self.assertEqual(searchDicts2(dictList2,"y"),False)
        self.assertEqual(searchDicts2(dictList2,"z"),"zero")
        self.assertEqual(searchDicts2(dictList2,"t"),None)

    # ------------ MY TESTS CASES FOR searchDicts2 ---------------
    # edge case
    def test_searchDicts2Edge(self):
        dictList2 = [(None,{})]
        self.assertEqual(searchDicts2(dictList2,"x"),None)
        self.assertEqual(searchDicts2(dictList2,"y"),None)
        self.assertEqual(searchDicts2(dictList2,"z"),None)
        self.assertEqual(searchDicts2(dictList2,"t"),None)

    #boundary cases
    def test_searchDicts2Boundary1(self):
        dictList2 = [(0,{"a":0,"y":True,"z":"zero"}), (0,{"x":1}), (2,{"y":False}), (1,{"x":3, "z":"three"}), (2,{"t": -9223372036854775807})]
        self.assertEqual(searchDicts2(dictList2,"y"),False)
        self.assertEqual(searchDicts2(dictList2,"a"),None)
        self.assertEqual(searchDicts2(dictList2,"t"),-9223372036854775807)

    def test_searchDicts2Boundary2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (10,{"y":9223372036854775807}), (1,{"x":3, "z":"three"}), (2,{})]
        self.assertEqual(searchDicts2(dictList2,"y"),9223372036854775807)
        self.assertEqual(searchDicts2(dictList2,"x"),None)
    # -----------------------------------------------------------

    def test_busStops(self):
        routes = {
            "Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
            "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
            "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
            "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
            "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]
        }
        self.assertEqual(busStops(routes,"Stadium"),['Lentil', 'Silver', 'Gray'])
        self.assertEqual(busStops(routes,"Bishop"),['Lentil', 'Wheat', 'Silver'])
        self.assertEqual(busStops(routes,"EECS"),[])
    
    # ------------------ MY TEST CASES FOR busStops() -------------------
    # edge case
    def test_busStopsEdge(self):
        self.assertEqual(busStops({},None),[])
    
    # boundary cases
    def test_busStopsBoundary1(self):
        self.assertEqual(busStops({'a':[1,2,3,4,5,6,7,8,9223372036854775807,0],2:[9223372036854775807]},9223372036854775807),['a',2])
    
    def test_busStopsBoundary2(self):
        self.assertEqual(busStops({1:[1,2,3,4,5,6,7,8,-9223372036854775807,0],"hello":[-9223372036854775807],3:[5,-12]},-9223372036854775807),[1,"hello"])
    # --------------------------------------------------------------------

    def test_palindromes(self):
        self.assertEqual(palindromes ('cabbbaccab'),['abbba', 'acca', 'baccab', 'bb', 'bbb', 'cabbbac', 'cc'] )
        self.assertEqual(palindromes ('bacdcabdbacdc') ,['abdba', 'acdca', 'bacdcab', 'bdb', 'cabdbac', 'cdc', 'cdcabdbacdc', 'dcabdbacd'])
        self.assertEqual(palindromes (' myracecars')  ,['aceca', 'cec', 'racecar'])

    # ---------------- MY TEST CASES FOR palindromes ---------------
    # edge cases
    def test_palindromesEdge(self):
        self.assertEqual(palindromes (''),[] )
    
    # boundary cases
    def test_palindromesBoundary1(self):
        self.assertEqual(palindromes ('aabbaa'),sorted(['aa','aabbaa','abba','bb']))
        self.assertEqual(palindromes ('dad'),sorted(['dad']))
        self.assertEqual(palindromes ('cdoabaqiw'),sorted(['aba']))
        self.assertEqual(palindromes ('aaaaa'),sorted(['aaaaa','aaaa','aaa','aa']))
        self.assertEqual(palindromes ('112211'),sorted(['112211','11','1221','22']))

    def test_palindromesBoundary2(self):
        self.assertEqual(palindromes ('aaabbac'),sorted(['aa','aaa','bb','abba']))

    # -------------------------------------------------------------

    class OddsEvens(object):
        def __init__(self,init):
            self.current = init
        def __next__(self):
            result = self.current
            self.current += 2
            return result
        def __iter__(self):
            return self

    #This function assumes that the first value in L is less than or equal to N.
    def getUntilN(self,L,N):
        tempL = []
        for item in L:
            tempL.append(item)
            if item>=N: break
        return tempL

    def test_interlaceIter(self):
    	#test 1
        iSequence = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(iSequence.__next__(),1)
        self.assertEqual(iSequence.__next__(),'a')
        self.assertEqual(iSequence.__next__(),2)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['b',3,'c',4,'d',5,'e',6,'f',7,'g'])

        #test2
        naturals = interlaceIter(self.OddsEvens(1),self.OddsEvens(2))
        self.assertEqual(naturals.__next__(),1)
        first20 = self.getUntilN(naturals,20)
        self.assertEqual(first20,[x for x in range(2,21)])
        self.assertEqual(naturals.__next__(),21)

    # ------------- MY TEST CASES FOR interlaceIter --------------
    # edge case
    def test_interlaceIterEdge(self):
    	#test 1
        rest = []
        try:
            iSequence = interlaceIter(iter([]),iter(""))
            for item in iSequence:
                rest.append(item)
        except StopIteration:
            pass
        self.assertEqual(rest,[])

    # boundary case 
    def test_interlaceIterBoundary1(self):
        iSequence = interlaceIter(iter([1,2,3,4]),iter("abcdefg"))
        self.assertEqual(iSequence.__next__(),1)
        self.assertEqual(iSequence.__next__(),'a')
        self.assertEqual(iSequence.__next__(),2)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['b',3,'c',4])
    
    def test_interlaceIterBoundary2(self):
        iSequence = interlaceIter(iter([9223372036854775807,-9223372036854775807,0,9999]),iter("abc"))
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,[9223372036854775807,'a',-9223372036854775807,'b',0,'c'])
    
    def test_interlaceIterBoundary3(self):
        iSequence = interlaceIter(iter('aaaabbb'),iter([1,2,3]))
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['a',1,'a',2,'a',3])
    # ----------------------------------------------------------------

    def test_typeHistogram(self):
    	#test 1
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 3), ('str', 2)])) 
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('str', 3), ('int', 2)])) 
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 2), ('str', 2)])) 
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), []) 
        #test 2
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        iSequence2 = interlaceIter(iSequence1, iter([(1,'a'),(2,'b'),(3,'c'),(4,'d')]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)),sorted([('int', 2), ('str', 2),('tuple',4)]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)), [])

    # -------------- MY TEST CASES FOR typeHistogram -------------------
    # edge case
    def test_typeHistogramEdge(self):
    	#test 1
        iSequence1 = interlaceIter(iter([0]),iter("abcdefg"))
        self.assertEqual(sorted(typeHistogram(iSequence1,9223372036854775807)), [('int',1)]) 

    # boundary case
    def test_typeHistogramBoundary1(self):
    	#test 1
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("AbcdEfgqw"))
        self.assertEqual(sorted(typeHistogram(iSequence1,-9223372036854775807)), [])

    def test_typeHistogramBoundary2(self):
    	#test 1
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,3,4,5,6,7,8,0]),iter("Abcdefg2,/"))
        self.assertEqual(sorted(typeHistogram(iSequence1,0)), [])
        self.assertEqual(sorted(typeHistogram(iSequence1,1)), [('int',1)])
        self.assertEqual(sorted(typeHistogram(iSequence1,2)), [('int',1),('str',1)])
        self.assertEqual(sorted(typeHistogram(iSequence1,-1)), [])
        self.assertEqual(sorted(typeHistogram(iSequence1,99999999)), [('int',8),('str',9)])
    # -----------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()

