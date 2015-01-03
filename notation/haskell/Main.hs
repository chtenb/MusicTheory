{-# LANGUAGE FlexibleInstances #-}
module Main where

instance Num a => Num (a -> a) where
  fromInteger n = (fromInteger n *)




-- It's implossible to implement whitespace operator, since function application has
-- the highest precedence. But with some hack, we may come close.

{-($$) x y = x * y-}
{-x ` ` y = x * y-}
{-( ) x y = x * y-}

main =
  do
    {-_4 <- 4 :: Int-}
    putStrLn $ show $ (3 (4 :: Int) :: Int)
    putStrLn "asdf"
