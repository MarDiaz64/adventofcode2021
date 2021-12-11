import java.io.File;  
import java.io.FileNotFoundException;  
import java.util.Scanner;
import java.util.ArrayList;
public class SquidBingo {
    public static void main(String[] args){
        try{
            ArrayList<BingoBoard> boards = new  ArrayList<BingoBoard>();
            File input = new File("test.txt");
            Scanner reader = new Scanner(input);
            String[] calledValues =reader.nextLine().trim().split(",");
            int counter =0;
            BingoBoard b = new BingoBoard();
            String firstEmptyLine=reader.nextLine(); //throw away
            while(reader.hasNextLine()){
                String line =reader.nextLine();
                if(!(line.isEmpty())){
                    String[] str =line.trim().split("\\s+");
                    for(int i=0; i<5;i++){
                        b.addItem(new BoardItem(Integer.parseInt(str[i])),i,counter);
                    }
                    counter++;
                }
                else{
                    boards.add(b);
                    b=new BingoBoard();
                    counter =0;
                }
            }
            boards.add(b);
            reader.close();
            System.out.print("Boards:");
            for(int i=0; i<boards.size();i++){
                boards.get(i).print();
            }
            System.out.print("\n");
            for(int i=0; i<calledValues.length;i++){
                int callVal= Integer.parseInt(calledValues[i]);
                for(int j=0; j<boards.size();j++){
                    BingoBoard winner = boards.get(j);
                    if((winner).checkBoard(callVal)){
                        System.out.println("Winning Call Value: "+callVal +" At board: "+j);
                        System.out.println("The Final Score is: "+winner.finalScore(callVal));
                        return;
                    }
                }
            }   
        }
        catch(FileNotFoundException e){
            System.out.println("Cannot find input");
            e.printStackTrace();
        }
    }
}
