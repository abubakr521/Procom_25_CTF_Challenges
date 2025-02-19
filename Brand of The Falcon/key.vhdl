-- key.vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ckey is
	Port (
		K : out STD_LOGIC_VECTOR(15 downto 0)
	);
end ckey;

architecture Behavioral of ckey is
    constant key : STD_LOGIC_VECTOR(15 downto 0) := "1011010110101100";
begin
    K <= key;
end Behavioral;



