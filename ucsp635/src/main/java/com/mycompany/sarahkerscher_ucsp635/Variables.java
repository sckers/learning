/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.sarahkerscher_ucsp635;

/**
 *
 * @author scker
 */
import java.util.Scanner;
public class Variables {
    public static void main(String[] args){
        Scanner scanstr = new Scanner(System.in);
        Scanner scanint = new Scanner(System.in);
        
        System.out.println("City: ");
        String city = scanstr.nextLine();
        System.out.println("Current temperature (F): ");
        int temperature = scanint.nextInt();
        System.out.println("Description: ");
        String description = scanstr.nextLine();
        
        int temp = (temperature - 32)*5/9;
        
        System.out.println();
        System.out.println(city+" is currently "+description+" and temperature is "+temp+"C.");
    }
}
