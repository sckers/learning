import java.util.regex.Pattern;
public class Sequence {
	
	//define properties of the sequence class
	//id -- sequence identifier
	//type -- type of sequence, DNA, RNA, or Protein
	//seq -- the sequence
	private String id;
	private String type;
	private String seq;
	
	public Sequence(){}
	
	public Sequence(String id,  String seq){
		this.id = id;
		this.seq = seq;	
	}
	
	public Sequence(String id, String type, String seq){
		this.id = id;
		this.type = type;
		this.seq = seq;
	}
	
	public void setID(String id){
		this.id = id;
	}
	
	public String getID(){
		return id;
	}
	
	public void setType(String type){
		this.type = type;
	}
	
	public String getType(){
		return type;
	}
	
	public void setSeq(String seq){
		this.seq = seq;
	}
	
	public String getSeq(){
		return seq;
	}
	
	public int getSize(){
		return seq.length();
	}
	
	// break a long sequence into chunks
	public String formatSeq(int len){
		
		String formatedSeq = "";
		while (seq.length()> len){
			formatedSeq += seq.substring(0, len) + "\n";
			seq = seq.substring(len);
		}
		// add the remaining part
		if (seq.length()>0){
			formatedSeq += seq;
		}		
		return formatedSeq;	
	}
	
	public int baseCount(char b) {
		int count = 0;
		for (int i= 0; i<seq.length(); i++){
			if (seq.charAt(i) == b) count++;
		}
		return count;
	}
			
	public String toString(){
		return String.format(">%s|%s\n%s\n", id, type, seq);
	}
	
	// method for DNA sequence validation
	public boolean validSeq(){
		return Pattern.matches("[ATCG]+", seq);
	}	
}
