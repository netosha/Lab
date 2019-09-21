package com.company;
import java.util.Random;
import java.lang.StrictMath;

public class Main{
    public static void main(String[] arg){
        /*First Task
         *
         * Создать одномерный массив p типа int.
         * Заполнить его чётными числами от 6 до 24 включительно в порядке возрастания.
         * */
        int[] z = new int[10];
        for(int i = 0; i < 10; i++){
            z[i] = 6 + (i*2);
        }

        /*Second Task
         *
         * Создать одномерный массив x типа double.
         * Заполнить его 20-ю случайными числами в диапазоне от -12.0 до 6.0.                 * */
        double[] x = new double[20];
        for(int i = 0; i < 20; i++){
            final double lowerValue = -12.0D;
            final double upperValue = 6.0D;
            Random random = new Random();
            x[i] = random.nextDouble() * (upperValue - lowerValue) + lowerValue;
        }

        /*Third Task
         *
         * Создать двумерный массив k размером 10x20.
         * etc.
         * */
        double q[][] = new double[10][20];

        for(int i = 0; i<10; i++){
            for(int j = 0; j<20; j++){
                double value = x[j];

                if(z[i] == 22){
                    /*Type of trigonometric functions output is double*/
                    q[i][j] = StrictMath.atan(StrictMath.cos(StrictMath.cbrt(StrictMath.sin(value))));
                }

                /*For specific P values*/
                else if(z[i] == 6 | z[i] ==8 | z[i] == 10 | z[i] == 16 | z[i] == 20 ){
                    q[i][j] = StrictMath.pow(((StrictMath.cos(value)/1)/(2/1)/3),2);
                }
                else{
                    q[i][j] =  StrictMath.exp(StrictMath.pow(StrictMath.tan(value), (StrictMath.tan(value) / (StrictMath.cos(value) -1)+1)));
                }

                System.out.printf("%.2f ", q[i][j]);
            }
            System.out.println("");
        }
    }
}