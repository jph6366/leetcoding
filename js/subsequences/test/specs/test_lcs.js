import { expect } from 'chai';
// import sinon from 'sinon';
import { Hirschberg_LCS_len, iterative_DP_LCS_len, iterative_DP_LCS_seq, memoize_LCS, naive_LCS, recursive_LCS } from '../../src/longestCommonSubsequence.js';

describe('naive longestCommonSubsequence', () => {
    it('should return 1 for a valid subsequence', () => {
        expect(naive_LCS('a', 'a')).to.equal(1);
    });

    it('should return 3 for a valid subsequence', () => {
        expect(naive_LCS('abcde', 'ace')).to.equal(3);
    });

    it('should return 3 for an invalid subsequence', () => {
        expect(naive_LCS('abc', 'abc')).to.equal(3);
    });

    it('should return 0 for an invalid subsequence', () => {
        expect(naive_LCS('abc', 'def')).to.equal(0);
    });

    it('should return 2 for an invalid subsequence', () => {
        expect(naive_LCS('oxcpqrsvwf', 'shmtulqrypy')).to.equal(2);
    });

});

describe('recursive longestCommonSubsequence', () => {
    it('should return 1 for a valid subsequence', () => {
        expect(recursive_LCS('a', 'a')).to.equal(1);
    });

    it('should return 3 for a valid subsequence', () => {
        expect(recursive_LCS('abcde', 'ace')).to.equal(3);
    });

    it('should return 3 for an invalid subsequence', () => {
        expect(recursive_LCS('abc', 'abc')).to.equal(3);
    });

    it('should return 0 for an invalid subsequence', () => {
        expect(recursive_LCS('abc', 'def')).to.equal(0);
    });

    it('should return 2 for an invalid subsequence', () => {
        expect(recursive_LCS('oxcpqrsvwf', 'shmtulqrypy')).to.equal(2);
    });

});


describe('memoize recursive longestCommonSubsequence', () => {
    it('should return 1 for a valid subsequence', () => {
        expect(memoize_LCS('a', 'a')).to.equal(1);
    });

    it('should return 3 for a valid subsequence', () => {
        expect(memoize_LCS('abcde', 'ace')).to.equal(3);
    });

    it('should return 3 for an invalid subsequence', () => {
        expect(memoize_LCS('abc', 'abc')).to.equal(3);
    });

    it('should return 0 for an invalid subsequence', () => {
        expect(memoize_LCS('abc', 'def')).to.equal(0);
    });

    it('should return 2 for an invalid subsequence', () => {
        expect(memoize_LCS('oxcpqrsvwf', 'shmtulqrypy')).to.equal(2);
    });

});


describe('tabulation of iterative longestCommonSubsequence', () => {
    it('should return 1 for a valid subsequence', () => {
        expect(iterative_DP_LCS_len('a', 'a')).to.equal(1);
    });

    it('should return 3 for a valid subsequence', () => {
        expect(iterative_DP_LCS_len('abcde', 'ace')).to.equal(3);
    });

    it('should return 3 for an invalid subsequence', () => {
        expect(iterative_DP_LCS_len('abc', 'abc')).to.equal(3);
    });

    it('should return 0 for an invalid subsequence', () => {
        expect(iterative_DP_LCS_len('abc', 'def')).to.equal(0);
    });

    it('should return 2 for an invalid subsequence', () => {
        expect(iterative_DP_LCS_len('oxcpqrsvwf', 'shmtulqrypy')).to.equal(2);
    });

});


describe(' return sequence for iterative longestCommonSubsequence', () => {
    it('should return 1 for a valid subsequence', () => {
        expect(iterative_DP_LCS_seq('a', 'a').length).to.equal(1);
    });

    it('should return 3 for a valid subsequence', () => {
        expect(iterative_DP_LCS_seq('abcde', 'ace').length).to.equal(3);
    });

    it('should return 3 for an invalid subsequence', () => {
        expect(iterative_DP_LCS_seq('abc', 'abc').length).to.equal(3);
    });

    it('should return 0 for an invalid subsequence', () => {
        expect(iterative_DP_LCS_seq('abc', 'def').length).to.equal(0);
    });

    it('should return 2 for an invalid subsequence', () => {
        expect(iterative_DP_LCS_seq('oxcpqrsvwf', 'shmtulqrypy').length).to.equal(2);
    });

});


describe(' return sequence for iterative longestCommonSubsequence', () => {
    it('should return 1 for a valid subsequence', () => {
        expect(Hirschberg_LCS_len('a', 'a')).to.equal(1);
    });

    it('should return 3 for a valid subsequence', () => {
        expect(Hirschberg_LCS_len('abcde', 'ace')).to.equal(3);
    });

    it('should return 3 for an invalid subsequence', () => {
        expect(Hirschberg_LCS_len('abc', 'abc')).to.equal(3);
    });

    it('should return 0 for an invalid subsequence', () => {
        expect(Hirschberg_LCS_len('abc', 'def')).to.equal(0);
    });

    it('should return 2 for an invalid subsequence', () => {
        expect(Hirschberg_LCS_len('oxcpqrsvwf', 'shmtulqrypy')).to.equal(2);
    });

});
