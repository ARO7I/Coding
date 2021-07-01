if [ -z ${ID} ] ; then
    echo 'set ${ID}!'
    return
fi

useradd -ms /bin/zsh ${ID}
adduser ${ID} sudo
adduser ${ID} users

su - ${ID} sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sed -r 's/exec zsh -l//g') &&\
                  git clone https://github.com/djui/alias-tips.git /home/${ID}/.oh-my-zsh/custom/plugins/alias-tips &&\
                  pip3 install -U pip==20.3.4 &&\
                  pip3 install -U pwntools &&\
                  git clone https://github.com/longld/peda.git /home/${ID}/.peda &&\
                  sed -ri 's/n\", \"a/ff\", \"a/g' /home/${ID}/.peda/lib/config.py &&\
                  git clone https://github.com/scwuaptx/Pwngdb.git /home/${ID}/.Pwngdb &&\
                  pip3 install -U capstone &&\
                  git clone https://github.com/JonathanSalwan/ROPgadget.git /home/${ID}/.ROPgadget &&\
                  curl -fLo /home/${ID}/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim &&\
                  git clone https://github.com/vim-airline/vim-airline.git /home/${ID}/.vim/plugged/vim-airline &&\
                  git clone https://github.com/vim-airline/vim-airline-themes.git /home/${ID}/.vim/plugged/vim-airline-themes &&\
                  git clone https://github.com/tpope/vim-fugitive.git /home/${ID}/.vim/plugged/vim-fugitive &&\
                  git clone https://github.com/jeetsukumaran/vim-buffergator.git /home/${ID}/.vim/plugged/vim-buffergator &&\
                  git clone https://github.com/preservim/nerdtree.git /home/${ID}/.vim/plugged/nerdtree &&\
                  git clone https://github.com/levelone/tequila-sunrise.vim.git /home/${ID}/.vim/plugged/tequila-sunrise.vim"

cp /script/zshrc /home/${ID}/.zshrc
cp /script/vimrc /home/${ID}/.vimrc
cp /script/gdbinit /home/${ID}/.gdbinit
chmod 755 /home/${ID}/.zshrc
chown ${ID}:users /home/${ID}/.zshrc
chmod 755 /home/${ID}/.vimrc
chown ${ID}:users /home/${ID}/.vimrc
chmod 755 /home/${ID}/.gdbinit
chown ${ID}:users /home/${ID}/.gdbinit

echo "1234\n1234\n" | passwd ${ID}
