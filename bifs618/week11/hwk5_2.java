/*BIFS 618
Homework 5, Question 2
File name: hwk5_2.java
Sarah Kerscher
*/

import org.biojava.bio.BioException;
import org.biojavax.bio.seq.RichSequence;
import org.biojavax.bio.seq.RichSequenceIterator;
import org.biojavax.bio.seq.RichSequence.IOTools;
import org.biojava.bio.seq.DNATools;
import org.biojava.bio.symbol.*;

import java.io.*;
import java.util.Scanner;
import javax.swing.JFileChooser;

public class hwk5_2{

    private static JFileChooser ourChooser = new JFileChooser(".");

    /**
    * Open a file through a FileChooser
    */
    public static BufferedReader openFile(){
        int retval = ourChooser.showOpenDialog(null);
        BufferedReader br = null;

        if (retval == JFileChooser.APPROVE_OPTION){
            File file = ourChooser.getSelectedFile();
            try {
              br = new BufferedReader(new FileReader(file));
            } catch (FileNotFoundException e) {
              System.out.println("trouble reading "+file.getName());
              e.printStackTrace();
            }
        }
        return br;
    }


    public static void main(String[] args) throws BioException{
        BufferedReader br = openFile();

        RichSequenceIterator it =  IOTools.readFastaDNA(br, null);

        while (it.hasNext()){
            RichSequence s = it.nextRichSequence();
            System.out.println("Accession: " + s.getAccession());

            SymbolList dnaSymbol = DNATools.createDNA(s.seqString());
            System.out.println("Protein Sequences: \nFrame 1: " +
                                DNATools.toProtein(dnaSymbol, 1, dnaSymbol.length()).seqString() + "\nFrame 2: " +
                                DNATools.toProtein(dnaSymbol, 2, dnaSymbol.length()).seqString() + "\nFrame 3: " +
                                DNATools.toProtein(dnaSymbol, 3, dnaSymbol.length()).seqString() + "\n\n");
        }
    }
}
