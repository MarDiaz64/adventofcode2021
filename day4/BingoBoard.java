public class BingoBoard {
    private int size;
    private BoardItem[][] board;
    public BingoBoard(){
        size=5;
        board = new BoardItem[size][size];
    }  
    public void addItem(BoardItem item,int i, int j){
        if(i>=0 && j>=0 && i<size && j<size){
            board[j][i]=item;
        }  
    }
    //false if no bingo or item doesn't exist, returns true if bingo
    public boolean checkBoard(int nextValue){
        for(int i=0; i<size;i++){
            for(int j=0; j<size;j++){
                if(board[i][j].getValue()==nextValue){
                    board[i][j].markUsed();
                    return bingo(i,j);
                }
            }
        }
        return false;
    }
    //check if bingo
    private boolean bingo(int col, int row){
        if(checkColumn(col)||checkRow(row)){
            return true;
        }
        return false;
    }
    //check column, if 1 in the column is not used, no bingo
    private boolean checkColumn(int col){
        for(int i=0; i<size;i++){
            if(!(board[col][i].isUsed())){
                return false;
            } 
        }
        return true;
    }
    //check row, if 1 in the row is not used, no bingo
    private boolean checkRow(int row){
        for(int i=0; i<size;i++){
            if(!(board[i][row].isUsed())){
                return false;
            } 
        }
        return true;
    }
    public int finalScore(int lastCalledNum){
        int counter=0;
        for(int i=0; i<size;i++){
            for(int j=0; j<size;j++){
                if(board[i][j].isUsed()){
                    counter+=board[i][j].getValue();
                }
            }
        }
        return counter*lastCalledNum;
    }
    public void print(){
        System.out.print("\n");
        for(int i=0; i<size;i++){
            for(int j=0; j<size;j++){
                System.out.print((board[i][j].toString())+" ");
            }
            System.out.print("\n");
        }
        
    }
}
