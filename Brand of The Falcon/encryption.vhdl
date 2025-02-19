-- encryption.vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity encryption is
	Port (
		D, K : in STD_LOGIC_VECTOR(15 downto 0);
		E : out STD_LOGIC_VECTOR(15 downto 0)
	);
end encryption;

architecture Behavioral of encryption is
begin
	process(D, K)
	begin
        for i in 0 to 15 loop
            E(i) <= D(i) XOR K(i);
        end loop;
        E(2) <= NOT K(2);
        E(7) <= NOT K(7);
        E(12) <= NOT K(12);
	end process;
end Behavioral;