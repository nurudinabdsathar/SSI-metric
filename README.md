# SSI-metric

This repository provides a simple code to calculate the Solution Stability Index (SSI), a number between 0 and 1 that tells you how stable your simulation results are across three mesh levels: coarse, medium, and fine.

---

## 🧠 What is SSI?

When you refine your mesh, your simulation results should become more stable. But how do you measure that? This is where SSI comes in. It tells you — using just the results — how stable things are.

No need to know your mesh size, no need to calculate accuracy orders, just give the 3 output values (e.g. force, pressure, drag).

---

## 📌 How to Calculate

Here’s how the SSI is calculated:

Step 1: average = abs((coarse + medium + fine) / 3)
Step 2: variation = abs(medium - coarse) + abs(fine - medium)
Step 3: penalty = 0.25 if the result is not consistent (i.e. it changes direction)
Step 4: SSI = 1 - (variation / average) - penalty


Final result is between 0 (very unstable) and 1 (very stable).

---

## 🛠️ How to Use This Code

If you have Python installed:

1. Open terminal / command prompt
2. Run:

```bash
python ssi.py

You will see something like:
SSI = 0.7000

Example
Let’s say your results for a parameter were:

Coarse: 10.2

Medium: 9.8

Fine: 10.0

The code will calculate:
SSI = 0.7000

Where Can You Use This?
CFD: Pressure, torque, lift, drag
FEM: Displacement, stress
Heat Transfer: Nusselt number, surface heat flux
Multiphysics: Any scalar quantity affected by grid density
Any simulation: if you have 3 values from mesh refinement, SSI works

Citation (optional)
If this code helps your research:
NA Settar, S Sarip, HM Kaidi, "Solution Stability Index (SSI): A Simple Post-Processing Metric for Evaluating Mesh-Induced Stability in CFD" – under review.
