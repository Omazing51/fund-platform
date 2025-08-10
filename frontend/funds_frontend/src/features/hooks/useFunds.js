import { useEffect, useState } from "react";
import { getAllFunds } from "../services/fundService";

export function useFunds() {
  const [funds, setFunds] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchFunds() {
      try {
        setLoading(true);
        const data = await getAllFunds();
        setFunds(data);
      } catch (err) {
        setError("Error al cargar los fondos");
      } finally {
        setLoading(false);
      }
    }
    fetchFunds();
  }, []);

  return { funds, loading, error };
}
