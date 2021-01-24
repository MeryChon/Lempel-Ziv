This is a simple implementation of Lempel-Ziv compression algorithm.
The implementation is based of pseudo code found here: https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/

Pseudo code for compression:
Initialize table with single character strings
<code>
P = first input character
WHILE not end of input stream
    C = next input character
    IF P + C is in the string table
        P = P + C
    ELSE
        output the code for P
        add P + C to the string table
        P = C
END WHILE
output code for P
</code>

Pseudo code for decompression
<code>
Initialize table with single character strings
 OLD = first input code
 output translation of OLD
 WHILE not end of input stream
     NEW = next input code
     IF NEW is not in the string table
            S = translation of OLD
            S = S + C
    ELSE
           S = translation of NEW
    output S
    C = first character of S
    OLD + C to the string table
    OLD = NEW
END WHILE
</code>