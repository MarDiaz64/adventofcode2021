public class BoardItem {
    private boolean used;
    private int value;
    
    public BoardItem(){
        value =0;
        used=false;
    }
    public BoardItem(int v){
        value=v;
        used=false;
    }
    public void markUsed(){
        used=true;
    }
    public boolean isUsed(){
        return used;
    }
    public int getValue(){
        return value;
    }
    public String toString(){
        if(used){
            return "\""+ value+"\"";
        }
        else{
            return ""+ value;
        }
        
    }
}
