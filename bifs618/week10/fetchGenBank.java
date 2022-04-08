import org.biojava.bio.BioException;
import org.biojavax.bio.db.ncbi.GenbankRichSequenceDB;
import org.biojavax.bio.seq.RichSequence;
import org.biojavax.bio.db.ncbi.GenpeptRichSequenceDB;

import java.util.Scanner;

public class fetchGenBank {

     public static void main(String[] args) {
             RichSequence rs = null;
             GenbankRichSequenceDB grsdb = new GenbankRichSequenceDB();
             GenpeptRichSequenceDB gprsdb = new GenpeptRichSequenceDB();
             Scanner input = new Scanner(System.in);

             try{
             // get data via GenBank accession number or gi number
                 System.out.println("Enter a GenBank accession number or gi number: ");
                 String id = input.nextLine();

                 System.out.println("DNA or protein?");
                 String type = input.nextLine();

                 if(type.equals("DNA")){
                   rs = grsdb.getRichSequence(id);
                   System.out.println(rs.getName()+" | "+rs.getDescription());
                   System.out.println(rs.seqString());
                 }

                 if(type.equals("protein")){
                   rs = gprsdb.getRichSequence(id);
                   System.out.println(rs.getName() + " | " + rs.getDescription());
                   System.out.println(rs.seqString());
                 }

                 System.out.println("\n\nAuthor: Sarah Kerscher");
             }
             catch(BioException be){
                 be.printStackTrace();
                 System.exit(-1);
             }
     }
}
