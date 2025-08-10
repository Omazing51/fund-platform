import { useFunds } from "../hooks/useFunds";
import FundsList from "../components/FundsList";

export default function FundsContainer() {
  const { funds, loading, error } = useFunds();

  const reloadFunds = () => {
    window.location.reload(); 
  };

  if (loading) return <p>Cargando fondos...</p>;
  if (error) return <p>{error}</p>;

  return <FundsList funds={funds} onSubscribed={reloadFunds} />;
}
