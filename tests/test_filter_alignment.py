#!/usr/bin/env python

__author__ = "Dan Knights"
__copyright__ = "Copyright 2010, The QIIME Project"
__credits__ = ["Greg Caporaso","Dan Knights"]
__license__ = "GPL"
__version__ = "0.92"
__maintainer__ = "Dan Knights"
__email__ = "danknights@gmail.com"
__status__ = "Release"

from cogent.util.unit_test import TestCase, main
from cogent import LoadSeqs
from cogent.core.alignment import DenseAlignment
from qiime.filter_alignment import apply_lane_mask, apply_gap_filter,\
 apply_lane_mask_and_gap_filter

class FilterAlignmentTests(TestCase):

    def setUp(self):
        """Init variables for the tests """
        self.aln1 = [\
            '>s1','ACC--T',\
            '>s2','AC---T',\
            '>s3','TCT--T',\
            '>s4','ACG--T',\
            '>s5','---A--'\
            ]
        self.aln2 = aln2_fasta.split('\n')
        self.aln2_lm = aln2_lm
        
    def test_apply_lane_mask_and_gap_filter_real(self):
        """apply_lane_mask_and_gap_filter: no error on full length seqs
        """
        # No error when applying to full-length sequence
        actual = apply_lane_mask_and_gap_filter(\
         self.aln2,self.aln2_lm)
        

    def test_apply_lane_mask_and_gap_filter(self):
        """apply_lane_mask_and_gap_filter: functions as expected
        """
        lm = '111111'
        expected = self.aln1.__iter__()
        for result in apply_lane_mask_and_gap_filter(self.aln1,lm,1.0):
            self.assertEqual(result,expected.next()+'\n')

        lm = None
        expected = self.aln1.__iter__()
        for result in apply_lane_mask_and_gap_filter(self.aln1,lm,1.0):
            self.assertEqual(result,expected.next()+'\n')
         
        # gap filter only
        lm = '111111'
        expected = [\
            '>s1','ACC-T',\
            '>s2','AC--T',\
            '>s3','TCT-T',\
            '>s4','ACG-T',\
            '>s5','---A-'\
            ].__iter__()

        for result in apply_lane_mask_and_gap_filter(self.aln1,lm):
            self.assertEqual(result,expected.next()+'\n')
         
        # lm filter only
        lm = '011111'
        expected = [\
         '>s1','CC--T',\
         '>s2','C---T',\
         '>s3','CT--T',\
         '>s4','CG--T',\
         '>s5','--A--'\
         ].__iter__()

        for result in apply_lane_mask_and_gap_filter(self.aln1,lm,1.0):
            self.assertEqual(result,expected.next()+'\n')
         
        # gap and lm filter
        lm = '011111'
        expected = [\
         '>s1','CC-T',\
         '>s2','C--T',\
         '>s3','CT-T',\
         '>s4','CG-T',\
         '>s5','--A-'\
         ].__iter__()

        for result in apply_lane_mask_and_gap_filter(self.aln1,lm):
            self.assertEqual(result,expected.next()+'\n')

    def test_apply_lane_mask(self):
        """ apply_lane_mask: functions as expected with varied lane masks
        """
        lm1 = '111111'
        expected = self.aln1.__iter__()
        for result in apply_lane_mask(self.aln1,lm1):
            self.assertEqual(result,expected.next()+'\n')

        lm2 = '000000'
        expected = [\
         '>s1','',\
         '>s2','',\
         '>s3','',\
         '>s4','',\
         '>s5',''\
         ].__iter__()

        for result in apply_lane_mask(self.aln1,lm2):
            self.assertEqual(result,expected.next()+'\n')
        
        lm3 = '101010'
        expected = [\
         '>s1','AC-',\
         '>s2','A--',\
         '>s3','TT-',\
         '>s4','AG-',\
         '>s5','---'\
         ].__iter__()

        for result in apply_lane_mask(self.aln1,lm3):
            self.assertEqual(result,expected.next()+'\n')


        lm4 = '000111'
        expected = [\
         '>s1','--T',\
         '>s2','--T',\
         '>s3','--T',\
         '>s4','--T',\
         '>s5','A--'\
         ].__iter__()

        for result in apply_lane_mask(self.aln1,lm4):
            self.assertEqual(result,expected.next()+'\n')

        
    def test_apply_gap_filter(self):
        """ apply_gap_filter: functions as expected with varied allowed_gap_frac
        """
        expected = self.aln1.__iter__()
                
        for result in apply_gap_filter(self.aln1,1.0):
            self.assertEqual(result,expected.next()+'\n')

        expected = [\
         '>s1','ACC-T',\
         '>s2','AC--T',\
         '>s3','TCT-T',\
         '>s4','ACG-T',\
         '>s5','---A-'\
         ].__iter__()

        for result in apply_gap_filter(self.aln1):
            self.assertEqual(result,expected.next()+'\n')


        expected = [\
         '>s1','ACCT',\
         '>s2','AC-T',\
         '>s3','TCTT',\
         '>s4','ACGT',\
         '>s5','----'\
         ].__iter__()

        for result in apply_gap_filter(self.aln1,0.75):
            self.assertEqual(result,expected.next()+'\n')

        expected = [\
         '>s1','ACCT',\
         '>s2','AC-T',\
         '>s3','TCTT',\
         '>s4','ACGT',\
         '>s5','----'\
         ].__iter__()

        for result in apply_gap_filter(self.aln1,0.40):
            self.assertEqual(result,expected.next()+'\n')


        expected = [\
         '>s1','ACT',\
         '>s2','ACT',\
         '>s3','TCT',\
         '>s4','ACT',\
         '>s5','---'\
         ].__iter__()

        for result in apply_gap_filter(self.aln1,0.30):
            self.assertEqual(result,expected.next()+'\n')

        
        expected = [\
         '>s1','',\
         '>s2','',\
         '>s3','',\
         '>s4','',\
         '>s5',''\
         ].__iter__()

        for result in apply_gap_filter(self.aln1,0.10):
            self.assertEqual(result,expected.next()+'\n')

        # the following tests were adapted from test_alignment.py in PyCogent

        aln = [\
            '>a','--A-BC-',\
            '>b','-CB-A--',\
            '>c','--D-EF-'\
            ]

        #default should strip out cols that are 100% gaps
        expected = [\
            '>a','-ABC',\
            '>b','CBA-',\
            '>c','-DEF'\
            ].__iter__()
        for result in apply_gap_filter(aln):
            self.assertEqual(result,expected.next()+'\n')

        # if allowed_gap_frac is 1, shouldn't delete anything
        expected = [\
            '>a','--A-BC-',\
            '>b','-CB-A--',\
            '>c','--D-EF-'\
            ].__iter__()
        for result in apply_gap_filter(aln,1):
            self.assertEqual(result,expected.next()+'\n')


        #if allowed_gap_frac is 0, should strip out any cols containing gaps
        expected = [\
            '>a','AB',\
            '>b','BA',\
            '>c','DE'\
            ].__iter__()
        for result in apply_gap_filter(aln,0):
            self.assertEqual(result,expected.next()+'\n')

        #intermediate numbers should work as expected
        expected = [\
            '>a','ABC',\
            '>b','BA-',\
            '>c','DEF'\
            ].__iter__()
        for result in apply_gap_filter(aln,0.4):
            self.assertEqual(result,expected.next()+'\n')
        expected = [\
            '>a','-ABC',\
            '>b','CBA-',\
            '>c','-DEF'\
            ].__iter__()
        for result in apply_gap_filter(aln,0.7):
            self.assertEqual(result,expected.next()+'\n')
        
    def test_apply_lane_mask_and_gap_filter_alternate_alignment(self):
        """apply_lane_mask_and_gap_filter: functions as expected with alt aln
        """
        aln = [\
         '>ACT009','AACT-',\
         '>ACT019','AACT-',\
         '>ACT011','-TCT-'\
         ]
        expected = aln.__iter__()
        for result in apply_lane_mask_and_gap_filter(aln,None,1.0):
            self.assertEqual(result,expected.next()+'\n')
        
        lm = '00111'
        expected = [\
         '>ACT009','CT',\
         '>ACT019','CT',\
         '>ACT011','CT'\
         ].__iter__()
        for result in apply_lane_mask_and_gap_filter(aln,lm):
            self.assertEqual(result,expected.next()+'\n')

aln2_fasta = """>1121 HalF20SW_57886 RC:1..219
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------A--AT-GT-A-T-A-GT---TAA--T-CT-G--C-C-CCA--TA-G------------------------------------------------------------------T-GG----AGG-AC-AA-CAG-------------------------T-T-A-----------------------GAA-A---TGA-CTG-CTAA-TA---CT-C--C-AT-A----------C--------------------T-C--C-T-T--C--T-----------------T----AT-C-----------------------------------------------------------------------------------------------------------------------A-TA-A--------------------------------------------------------------------------------------------------------------------------------------G-T-T----A---------------A--G-T-C-G-G-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------GAAA--G-T----------------------------------------------------------------------------------------------------------------------------------------TTT------------------------------------------------------------------------------------------------------------------------------------T---C-G--------------C----T-A---T-GG-G---AT---G-A-----G-ACT-ATA--T-CGT--A------TC--A--G-CT-A----G---TTGG-T-A-AG-G-T----AAT-GG-C-T-T-ACCA--A-GG-C-T--A-TG-A------------CGC-G-T------AA-CT-G-G-TCT-G-AG----A--GG-AT--G-AT-C-AG-TCAC-A-TTGGA--A-C-TG-A-GA-C-AC-G-G-TCCAA------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
>1122 HalF02FT_61708 RC:7..217
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------G--C-C-TGG--TA-G------------------------------------------------------------------T-GG----GGG-AT-AA-CTA-------------------------T-T-G-----------------------GAA-A---CGA-TAG-CTAA-TA---CC-G--C-AT-A---------------------------------A-TA-G-C--A--G-----------------TT---GT-T-----------------------------------------------------------------------------------------------------------------------G-CA-T--------------------------------------------------------------------------------------------------------------------------------------G-A-C--A-A---------------C--T-G-T-T-T-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------GAAA--G-G-T-GC-----------------------------------------------------------------------------------------------------------------------------------AAT-T----------------------------------------------------------------------------------------------------------------------------G-CA--C---C-A--------------C----T-A---C-CA-G---AT---G-G-----A-CCT-GCG--T-TGT--A------TT--A--G-CT-A----G---TTGG-T-G-GG-G-T----AAC-GG-C-T-C-ACCA--A-GG-C-G--A-CG-A------------TAC-A-T------AG-CC-G-A-CCT-G-AG----A--GG-GT--G-AT-C-GG-CCAC-A-CTGGG--A-C-TG-A-GA-C-AC-G-G-CCCAG------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

aln2_lm = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110111101011001110100101101011001000010100111111010110101110111010111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011010110101101001000000000000011101111101001101101010101100011100101101001010111001101000000000000000000000000000000000000000000000000000000000000000000101100001110110110111000000000000000000000000010101000000000000000000000001110100011101110111101100011010010110100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100001010001011010001100010100000101110111001011100100000011001001011010000100011110101011010100001110110101010111100101101010010110100000000000011101010000001101101010111010110000100110110010110101101111010111110010101101011010110101011111101111011101001010101011010110101011000110101011101111101011010110011011010000101011010110110110111101111010110100010101001001101010010010101011000001101100000000010101010101001000110101110000000011011010100101110000110100100000000000000000000000000000000000000000000000000000000000000000001101101010110101101000000000110000000000011111011101101011100010110111100111100101000100111100010110011011001100011011011101110101011011110101110110110100101001111011100001101111011001011010101010000000000001001011010101011000010101010001011101101011011001101110100000000000000000000000000000000000000000000000000000000000000000000110101100000000000000000000000000000000000000000000000000000000000000000000000001101010110110100001010101010100000000100110101010101011100101010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001010101010101000001011001101010000000000001011010110100001100111101110101100110101110111111011011101111010110101110011010110101101100100100110111010010100010000100101011111000000101101100000000000000000000000000000000000000000000000000000000000000110101010011001100000110110110010101110011010100000000000000101111011101010111100110111101011101000001101010111010100001011001010111010111001011110110011011000000000101100100101011010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101010101101000000110010000110111001101010100100110110010000101110111010101101110110001110000010100101010101110100111011110111000000000111101110111110101011110000101001010101110110100100110110100110111011011110101011101111010110101101010110110101101111101101011010101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001010101010111101101110110011101110101101100010110110100111011011101011010110110110111110110000000010111011101011101010110011001011110010101010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101001100000000000000010101010101101001101010111001010000000000000000000000000000000000001010001110000000000000000000000000000000000101010100101011010011101001111010111101110011110100011101010101010101110000110100110101011011011011101111101001100111110001011110101001011101101100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000101010101001011110100100000000000000000000000000000000000000010110101000000000001001010110001000000000010011101000000101011111011010101010111011100000000111010111110110010111101101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010111110101010110101101111101101011001011011010101000011101101010100000001100111011010110101110111101011111111101111000011111110111011100000100011001110110110100100011101011011011100101110000001001011100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111001100111010000101110110111000000000000000000000000110011101111011011101111111110111110111100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

if __name__ == "__main__":
    main()
