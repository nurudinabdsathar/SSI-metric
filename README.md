# Solution Stability Index (SSI) Calculator

This is a lightweight Python tool to calculate the **Solution Stability Index (SSI)** — a dimensionless number from 0 to 1 that quantifies the stability of simulation results across three mesh resolutions.

---

## 🧠 What is SSI?

When running simulations (e.g. CFD, FEM), mesh refinement should produce more stable results. SSI evaluates this stability **without needing mesh size or grid spacing** — you only need the output values.

### Formula:
1. **Average** = (coarse + medium + fine) / 3
2. **Variation** = |medium - coarse| + |fine - medium|
3. **Penalty** = 0.25 (if the result is inconsistent in direction)
4. **SSI** = 1 - (variation / average) - penalty

SSI is clamped to 0 if negative.

---

## 🧪 Example

Input:
```
Coarse = 10.2
Medium = 9.8
Fine = 10.0
```

Output:
```
SSI = 0.6 (Nearly Stable)
```

---

## ⚙️ How to Run

You need Python 3.x installed.

```bash
python SSI.py
```

Follow the on-screen prompts. You’ll be asked to enter:
- Coarse value
- Medium value
- Fine value

Then the SSI result and stability classification will be shown.

---

## ⚠️ Note
- Always enter **dimensionless coefficients**, like:
  - Ct (Torque Coefficient)
  - Cp (Pressure Coefficient)
  - Nu (Nusselt Number)
- **DO NOT** enter raw values like force, pressure, etc.

---

## 📄 Output Classification

| SSI Range        | Classification                     |
|------------------|-------------------------------------|
| 0                | Clamped to 0 (Complete Instability) |
| 0 < SSI < 0.29   | Unstable                            |
| 0.29 – 0.75      | Nearly Stable                       |
| > 0.75           | Stable                              |

---

## 📁 File Structure

- `SSI.py` – the main interactive CLI tool
- No dependencies beyond built-in Python functions

---

## 👨‍🔬 Author

Developed as part of a CFD mesh sensitivity analysis project. For technical inquiries or permission to reuse, please contact the original author.

If you use this tool in your research, please cite the associated journal article (once accepted):
NA Settar, S Sarip, HM Kaidi, Solution Stability Index (SSI): A Simple Post-Processing Metric for Evaluating Mesh-Induced Stability in CFD, under review.
