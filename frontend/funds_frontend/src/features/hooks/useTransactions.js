import { useEffect, useState } from "react";
import { getTransactions } from "../services/transactionService"; 

export function useTransactions(limit = 10) {
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getTransactions(limit)
      .then((data) => {
        setTransactions(data);
        setLoading(false);
      })
      .catch(() => {
        setError("Error al cargar transacciones");
        setLoading(false);
      });
  }, [limit]);

  return { transactions, loading, error };
}
