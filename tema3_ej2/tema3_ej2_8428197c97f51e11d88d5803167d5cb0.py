# crea la clase Vector y completa el código de la función suma_vectores usándola
public class Vector {
    private double x;
    private double y;
    private double z;

    public Vector(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double norma() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public static Vector suma_vectores(Vector v1, Vector v2) {
        return new Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z);
    }

    public Vector suma(Vector v) {
        return new Vector(x + v.x, y + v.y, z + v.z);
    }          