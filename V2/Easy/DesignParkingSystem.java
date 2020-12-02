class ParkingSystem {
    private int big;
    private int medium;
    private int small;
    
    private boolean big_a = false;
    private boolean med_a = false;
    private boolean small_a = false;
    
    
    public ParkingSystem(int big, int medium, int small) {
        this.big = big;
        this.medium = medium;
        this.small = small; 
        this.big_a = false;
        this.med_a = false;
        this.small_a = false;
    }
    
    public boolean addCar(int carType) {
          
        switch(carType)
        {
            case 1:
                if ((this.big > 0) && (big_a == false))
                {
                    this.big -= 1;
                    if (this.big == 0)
                        big_a = true;
                    return true;
                }
                else
                    return false;
            case 2:
                if ((this.medium > 0) && (med_a == false))
                {
                    this.medium -= 1;
                    if(this.medium == 0)
                        med_a = true;
                    return true;
                }
                else
                    return false;
            case 3:
                if ((this.small > 0) && (small_a == false))
                {
                    this.small -= 1;
                    if (this.small == 0)
                        small_a = true;
                    return true;
                }
                else
                    return false;
            default:
                return false;
        }
       
}
}
    

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */