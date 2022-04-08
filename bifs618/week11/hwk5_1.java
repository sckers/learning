/*BIFS 618
Homework 5, Question 1
File name: hwk5_1.java
Sarah Kerscher
*/

import org.biojava.bio.BioException;
import org.biojavax.bio.seq.RichSequence;
import org.biojavax.bio.seq.RichSequenceIterator;
import org.biojavax.bio.seq.RichSequence.IOTools;

import java.io.*;
import java.util.Scanner;
import javax.swing.JFileChooser;

public class hwk5_1{

  private static JFileChooser ourChooser = new JFileChooser(".");

  // read in sequence file GenBank_seq.gb
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

  // process sequence file
  public static void main(String[] args) throws BioException{
      BufferedReader br = openFile();

      RichSequenceIterator it =  IOTools.readGenbankDNA(br, null);

      while (it.hasNext()){
          RichSequence s = it.nextRichSequence();
          System.out.println("Accession: " + s.getAccession() +
                            "; Length: " + s.length() + "; Description: " +
                            s.getDescription());
          System.out.println("Sequence: \n" + s.seqString() + "\n\n");
      }
  }
}
