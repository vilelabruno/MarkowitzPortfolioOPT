/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package portfoliotheory;

import ilog.concert.IloException;
import ilog.concert.IloLinearNumExpr;
import ilog.concert.IloNumExpr;
import ilog.concert.IloNumVar;
import ilog.cplex.IloCplex;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.Vector;

/**
 *
 * @author rmachado
 */
public class PortfolioTheory {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException, IloException, IOException {
        String filePath = "shDf.txt";
        File file = new File(filePath);

        BufferedReader br = new BufferedReader(new FileReader(file));
        
        // natural variables
        int n = 211; // number of shares
        int A = 1; // risk index
        
        String st = br.readLine();
        String[] shares = new String[n]; // share names
        for (int i = 0; i < n; i++) {
            shares[i] = st.split(",")[i];
        }
        
        st = br.readLine();
        Double[] mi = new Double[n]; // share's return mean
        for (int i = 0; i < n; i++) {
            mi[i] = Double.parseDouble(st.split(",")[i]);
        }
        
        Double[][] sigma = new Double[n][n]; // correlation matrix between shares
        for (int i = 0; i < n; i++) {
            st = br.readLine();
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    sigma[i][j] = 1.0;
                } else if (j < i) {
                    sigma[i][j] = Double.parseDouble(st.split(",")[j]);
                } else {
                    sigma[i][j] = Double.parseDouble(st.split(",")[j-1]);
                }
            }
        }
        
        // create model
        IloCplex model = new IloCplex();
        
        // decision variables
        IloNumVar x[] = new IloNumVar[n];
        for (int i = 0; i < n; i++) {
            x[i] = model.numVar(0, 1);
        }
        
        // restrictions
        IloLinearNumExpr rest = model.linearNumExpr();
        for (int i = 0; i < n; i++) {
            rest.addTerm(x[i], 1);
        }
        model.addEq(rest, 1);
        
        for (int i = 0; i < n; i++) {
            IloLinearNumExpr rest2 = model.linearNumExpr();
            rest2.addTerm(x[i], 1);
            model.addGe(rest2, 0.0);
        }
        
        // objective function
        
//        IloNumExpr obj = model.numExpr();
//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < n; j++) {
//                IloNumExpr objAux = model.prod(sigma[i][j], x[i], x[j]);
//                obj = model.sum(obj, objAux);
//            }
//        }
        
        Vector<IloNumExpr> todas = new Vector<IloNumExpr>();
        IloNumExpr[][] exp = new IloNumExpr[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                exp[i][j] = model.prod(sigma[i][j], x[i], x[j]);
                todas.add(exp[i][j]);
            }
        }
        Object[] alinha = todas.toArray();
        IloNumExpr[] alinhaCorr = new IloNumExpr[alinha.length];
        for (int i = 0; i < alinha.length; i++) {
            alinhaCorr[i] = (IloNumExpr)alinha[i];
        }
        IloNumExpr todasExpr = model.sum(alinhaCorr);
        
        IloLinearNumExpr exp2 = model.linearNumExpr();
        for (int i = 0; i < n; i++) {
            exp2.addTerm((-1)*A*mi[i], x[i]);
        }
        
        IloNumExpr obj = model.sum(todasExpr, exp2);
        model.add(model.minimize(obj));
        
        // parameter
        model.setParam(IloCplex.Param.SolutionTarget, 3);
        
        if (model.solve()) {
            System.out.println("Objective Value:");
            System.out.println(model.getObjValue());
            System.out.println("Status:");
            System.out.println(model.getStatus());
            System.out.println("Shares:");
            for (int i = 0; i < n; i++) {
                System.out.println(i+"- "+shares[i]+": "+truncateDecimal(model.getValue(x[i])*100, 2));
            }
        }
    }

    private static BigDecimal truncateDecimal(double x, int numberofDecimals) {
        if (x > 0) {
            return new BigDecimal(String.valueOf(x)).setScale(numberofDecimals, BigDecimal.ROUND_FLOOR);
        } else {
            return new BigDecimal(String.valueOf(x)).setScale(numberofDecimals, BigDecimal.ROUND_CEILING);
        }
    }
}
