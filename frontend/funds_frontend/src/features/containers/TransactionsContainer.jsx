import { useTransactions } from "../hooks/useTransactions";
import TransactionsTable from "../components/TransactionTable";

export default function TransactionsContainer() {
  const { transactions, loading, error } = useTransactions(10);

  if (loading) return <p>Cargando transacciones...</p>;
  if (error) return <p>{error}</p>;

  return <TransactionsTable transactions={transactions} />;
}
