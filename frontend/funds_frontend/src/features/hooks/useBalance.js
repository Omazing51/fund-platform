import { useState, useEffect } from "react";
import { getBalance } from "../services/accountService";

export function useBalance() {
  const [balance, setBalance] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getBalance()
      .then((data) => {
        setBalance(Number(data.Balance)); 
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message || "Error al obtener saldo");
        setLoading(false);
      });
  }, []);

  return { balance, loading, error };
}
